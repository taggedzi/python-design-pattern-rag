import sys
import argparse
import logging
import time
import re
from pathlib import Path
from typing import List, Optional

try:
    import ollama
except ImportError:
    ollama = None

# Configure logging
def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s] %(levelname)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    return logging.getLogger("rag_chunker")

logger = setup_logging()

SYSTEM_PROMPT = (
    "You are a professional Python code annotator.\n"
    "Take the following Python code and return exactly three sections in Markdown format, in this order:\n"
    "1. A fenced code block (```python) with the full improved code including docstrings.\n"
    "2. A section heading '## Summary' followed by a brief description (1-2 sentences).\n"
    "3. A section heading '## Docstrings' followed by a bullet list of all added or improved docstrings.\n"
    "Use single blank lines only where required."  
)

# Retry and spacing helpers
def normalize_spacing(text: str) -> str:
    return re.sub(r'\n{3,}', '\n\n', text.strip())

# Core enhancement call
def enhance_code(code: str, model: str, retries: int, delay: float) -> Optional[str]:
    if ollama is None:
        logger.error("Ollama package not installed.")
        return None
    if not hasattr(ollama, 'chat'):
        logger.error("Ollama package missing `chat` API.")
        return None
    for i in range(1, retries + 1):
        try:
            resp = ollama.chat(
                model=model,
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are a professional Python code annotator.\n"
                            "Return exactly the following sections:\n"
                            "1. A full enhanced Python code block with docstrings\n"
                            "2. ## Summary\n"
                            "3. ## Docstrings\n"
                            "No commentary or extra explanation."
                        )
                    },
                    {
                        "role": "user",
                        "content": code.strip()
                    }
                ]
            )
            content = resp.get('message', {}).get('content', '').strip()
            return normalize_spacing(content)
        except Exception as e:
            logger.warning(f"Enhancement attempt {i}/{retries} failed: {e}")
            time.sleep(delay)
    logger.error("All enhancement attempts failed.")
    return None

# Write markdown chunk
def write_markdown(file_path: Path, md: str, output_dir: Path) -> None:
    rel = file_path.relative_to(args.source)
    chunk_name = rel.with_suffix('').as_posix().replace('/', '_').replace('\\', '_') + '.md'
    out = output_dir / chunk_name
    front_matter = f"---\nfile: {rel.as_posix()}\nchunk: {chunk_name}\n---\n\n"
    out.write_text(front_matter + md + '\n')
    logger.info(f"Wrote chunk: {out}")

# Process a single file
def process_file(file_path: Path, output_dir: Path, model: str, retries: int, delay: float) -> bool:
    logger.info(f"Processing {file_path}")
    try:
        code = file_path.read_text(encoding='utf-8')
    except Exception as e:
        logger.error(f"Failed reading {file_path}: {e}")
        return False
    enhanced = enhance_code(code, model, retries, delay)
    if not enhanced:
        logger.error(f"Enhancement failed for {file_path}")
        return False
    # Quick validation
    if '```python' not in enhanced or '## Summary' not in enhanced or '## Docstrings' not in enhanced:
        logger.error(f"Output format invalid for {file_path}")
        return False
    write_markdown(file_path, enhanced, output_dir)
    return True

# Main orchestration
def main():
    global args
    parser = argparse.ArgumentParser(
        description="Chunk Python files into Markdown with AI-enhanced docstrings for RAG ingestion"
    )
    parser.add_argument('source', help='Path to .py file or directory')
    parser.add_argument('output', help='Directory to write .md chunks')
    parser.add_argument('--model', default='pattern-rag-gen:latest', help='Ollama model name')
    parser.add_argument('--retries', type=int, default=3, help='Enhancement retry count')
    parser.add_argument('--delay', type=float, default=1.0, help='Delay between retries (s)')
    args = parser.parse_args()

    source = Path(args.source)
    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Gather files
    if source.is_file() and source.suffix == '.py':
        files = [source]
    else:
        files = list(source.rglob('*.py'))
    logger.info(f"Found {len(files)} file(s) to process.")

    failures: List[Path] = []
    for f in files:
        success = process_file(f, output_dir, args.model, args.retries, args.delay)
        if not success:
            failures.append(f)

    # Log failures
    if failures:
        log_path = output_dir / 'failed_chunks.log'
        with log_path.open('w', encoding='utf-8') as lf:
            for f in failures:
                lf.write(f"{f.as_posix()}\n")
        logger.warning(f"{len(failures)} failure(s). See {log_path}")
    else:
        logger.info("All files processed successfully.")

if __name__ == '__main__':
    main()
