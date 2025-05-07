#!/usr/bin/env python3
import sys
import argparse
import json
import logging
import time
import subprocess
from typing import Optional, Tuple, List
import re
from pathlib import Path
import ollama

# --- Directory setup ---
script_dir = Path(__file__).resolve().parent
project_root = script_dir.parent


def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='[%(asctime)s] %(levelname)s: %(message)s'
    )
    return logging.getLogger(__name__)

logger = setup_logging()


# System prompt for structured JSON output
def get_system_prompt() -> str:
    return (
        "You are a professional Python code summarizer. "
        "Given the Python source code, return a JSON object with two keys: "
        "`summary` (a 1-2 sentence summary) and `docstrings` (a list of strings, each representing a suggested docstring for a class or function). "
        "Respond with valid JSON only, no additional text."
    )

def annotate_code(
    code: str,
    model: str
) -> Optional[Tuple[str, List[str]]]:
    """
    Call Ollama chat API once to annotate the Python code.
    Returns a tuple (summary, docstrings) on success, or None on failure.
    """
    if ollama is None or not hasattr(ollama, 'chat'):
        logger.error("Ollama package with chat API is required.")
        return None

    try:
        resp = ollama.chat(
            model=model,
            messages=[
                {"role": "system", "content": get_system_prompt()},
                {"role": "user",   "content": code},
            ]
        )
        content = resp.get('message', {}).get('content', '').strip()
        if not content.startswith('{'):
            start = content.find('{')
            end = content.rfind('}')
            if start != -1 and end != -1:
                content = content[start:end+1]

        data = json.loads(content)
        summary = data.get('summary', '').strip()
        docstrings = [d.strip() for d in data.get('docstrings', []) if d.strip()]
        return summary, docstrings

    except Exception as e:
        logger.warning(f"Annotation failed: {e}")
        return None

def write_chunk(file_path: Path, summary: str, docstrings: list, output_dir: Path) -> Path:
    """
    Write the annotated chunk to Markdown and return its path.
    """
    # uses module-level source_dir set in main()
    rel = file_path.relative_to(source_dir)
    chunk_name = rel.with_suffix('').as_posix().replace('/', '_').replace('\\', '_') + '.md'
    out_path = output_dir / chunk_name

    front = f"---\nfile: {rel.as_posix()}\nchunk: {chunk_name}\n---\n\n"
    code_block = f"```python\n{file_path.read_text(encoding='utf-8')}\n```\n\n"
    summary_md = f"## Summary\n{summary}\n\n"
    doc_md = "## Docstrings\n" + ''.join(f"- {d}\n" for d in docstrings) + "\n"

    out_path.write_text(front + code_block + summary_md + doc_md, encoding='utf-8')
    logger.info(f"Wrote chunk: {out_path}")
    return out_path


def validate_chunk(md_path: Path) -> list:
    """
    Return a list of missing sections if any: ['code block', 'summary', 'docstrings']
    """
    text = md_path.read_text(encoding='utf-8')
    missing = []
    if not re.search(r'```python[\s\S]+?```', text):
        missing.append('code block')
    if not re.search(r'^## Summary', text, re.MULTILINE):
        missing.append('summary')
    if not re.search(r'^## Docstrings', text, re.MULTILINE):
        missing.append('docstrings')
    return missing


def generate_index(chunks_dir: Path, index_file: Path):
    """
    Invoke the summary_index_generator to build the JSON index.
    """
    index_script = script_dir / 'summary_index_generator.py'
    if not index_script.exists():
        logger.warning(f"Index script not found: {index_script}")
        return False
    result = subprocess.run([
        sys.executable,
        str(index_script),
        str(chunks_dir),
        str(index_file)
    ])
    if result.returncode == 0:
        logger.info(f"Summary index created at {index_file}")
        return True
    else:
        logger.error("Failed to generate summary index.")
        return False

def main():
    global source_dir
    parser = argparse.ArgumentParser(
        description="RAG chunker: processes Python files into Markdown chunks with retry logic."
    )
    parser.add_argument('--source',
        default=str(project_root / 'patterns'),
        help='Directory of Python source patterns')
    parser.add_argument('--output',
        default=str(project_root / 'chunks'),
        help='Directory to write Markdown chunks')
    parser.add_argument('--model',
        default='pattern-rag-gen:latest',
        help='Ollama model name')
    parser.add_argument('--retries',
        type=int, default=3,
        help='Max annotation retries per file')
    parser.add_argument('--delay',
        type=float, default=1.0,
        help='Seconds to wait between retries')
    parser.add_argument('--index',
        default=str(project_root / 'summary_index.json'),
        help='Path for the summary JSON index')
    args = parser.parse_args()

    # assign module-level for write_chunk
    source_dir = Path(args.source)
    output_dir = Path(args.output)
    index_file = Path(args.index)
    failures_log = output_dir / 'failed_chunks.log'

    # clear or create output_dir
    if output_dir.exists():
        for item in output_dir.iterdir():
            if item.is_file():
                item.unlink()
    else:
        output_dir.mkdir(parents=True)

    py_files = sorted(source_dir.rglob('*.py'))
    logger.info(f"Found {len(py_files)} Python files to process in {source_dir}.")

    failures = []
    for file_path in py_files:
        logger.info(f"Processing {file_path.relative_to(source_dir)}")
        attempt = 1
        success = False
        while attempt <= args.retries:
            result = annotate_code(file_path.read_text(encoding='utf-8'), args.model)
            if result:
                summary, docstrings = result
                md_path = write_chunk(file_path, summary, docstrings, output_dir)
                missing = validate_chunk(md_path)
                if not missing:
                    success = True
                    break
                else:
                    logger.warning(f"Attempt {attempt}: missing {missing}")
            else:
                logger.warning(f"Attempt {attempt}: no annotation result")
            attempt += 1
            time.sleep(args.delay)

        if not success:
            failures.append(file_path.relative_to(source_dir))
            logger.error(f"Failed to process {file_path} after {args.retries} attempts")

    # write failures log
    if failures:
        with failures_log.open('w', encoding='utf-8') as lf:
            for f in failures:
                lf.write(f"{f.as_posix()}\n")
        logger.warning(f"{len(failures)} file(s) failed; see {failures_log}")
    else:
        logger.info("All files processed successfully.")

    # generate summary index
    generate_index(output_dir, index_file)

    sys.exit(1 if failures else 0)

if __name__ == '__main__':
    main()



