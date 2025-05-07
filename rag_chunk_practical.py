import sys
import argparse
import logging
import time
import json
from pathlib import Path
from typing import List, Tuple, Optional

try:
    import ollama
except ImportError:
    ollama = None

# Setup logging
def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s] %(levelname)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    return logging.getLogger("rag_chunker_practical")

logger = setup_logging()

# System prompt for structured JSON output
def get_system_prompt() -> str:
    return (
        "You are a professional Python code summarizer. "
        "Given the Python source code, return a JSON object with two keys: "
        "`summary` (a 1-2 sentence summary) and `docstrings` (a list of strings, each representing a suggested docstring for a class or function). "
        "Respond with valid JSON only, no additional text."
    )

# Call Ollama to get summary and docstrings
def annotate_code(code: str, model: str, retries: int, delay: float) -> Optional[Tuple[str, List[str]]]:
    if ollama is None or not hasattr(ollama, 'chat'):
        logger.error("Ollama package with chat API is required.")
        return None
    prompt = get_system_prompt()
    for attempt in range(1, retries + 1):
        try:
            resp = ollama.chat(
                model=model,
                messages=[
                    {"role": "system", "content": prompt},
                    {"role": "user", "content": code}
                ]
            )
            content = resp.get('message', {}).get('content', '').strip()
            # Extract JSON substring if extra text present
            if not content.startswith('{'):
                start = content.find('{')
                end = content.rfind('}')
                if start != -1 and end != -1:
                    content = content[start:end+1]
            data = json.loads(content)
            summary = data.get('summary', '').strip()
            docstrings = [d.strip() for d in data.get('docstrings', []) if d.strip()]
            return summary, docstrings
        except json.JSONDecodeError as jde:
            logger.warning(f"JSON parse failed (attempt {attempt}): {jde}")
        except Exception as e:
            logger.warning(f"Annotation attempt {attempt} failed: {e}")
        time.sleep(delay)
    logger.error("All annotation attempts failed.")
    return None

# Write markdown chunk
def write_chunk(file_path: Path, summary: str, docstrings: List[str], output_dir: Path) -> None:
    rel = file_path.relative_to(args.source_dir)
    chunk_name = rel.with_suffix('').as_posix().replace('/', '_').replace('\\', '_') + '.md'
    out_path = output_dir / chunk_name
    front = f"---\nfile: {rel.as_posix()}\nchunk: {chunk_name}\n---\n\n"
    code_block = f"```python\n{file_path.read_text(encoding='utf-8')}\n```\n\n"
    summary_md = f"## Summary\n{summary}\n\n"
    doc_md = "## Docstrings\n" + ''.join([f"- {d}\n" for d in docstrings]) + "\n"
    out_path.write_text(front + code_block + summary_md + doc_md, encoding='utf-8')
    logger.info(f"Wrote chunk: {out_path}")

# Main processing
def main():
    global args
    parser = argparse.ArgumentParser(description="Practical RAG chunker: extracts code + structured annotations.")
    parser.add_argument('source', help='.py file or directory to process')
    parser.add_argument('output', help='Output directory for .md chunks')
    parser.add_argument('--model', default='pattern-rag-gen:latest', help='Ollama model name')
    parser.add_argument('--retries', type=int, default=2, help='Number of annotation retries')
    parser.add_argument('--delay', type=float, default=1.0, help='Delay between retries')
    args = parser.parse_args()

    source = Path(args.source)
    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)
    args.source_dir = source  # store for write_chunk

    # Gather Python files
    if source.is_file() and source.suffix == '.py':
        files = [source]
    else:
        files = list(source.rglob('*.py'))
    logger.info(f"Found {len(files)} Python file(s) to process.")

    failures = []
    for f in files:
        logger.info(f"Annotating {f}")
        result = annotate_code(f.read_text(encoding='utf-8'), args.model, args.retries, args.delay)
        if result:
            summary, docstrings = result
            write_chunk(f, summary, docstrings, output_dir)
        else:
            failures.append(f)

    if failures:
        log_file = output_dir / 'failed_chunks.log'
        with log_file.open('w', encoding='utf-8') as lf:
            for f in failures:
                lf.write(f"{f.as_posix()}\n")
        logger.warning(f"{len(failures)} failure(s). See {log_file}")
    else:
        logger.info("All files processed successfully.")

if __name__ == '__main__':
    main()
