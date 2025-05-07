
import os
import ast
import re
import time
import logging
import argparse
from pathlib import Path
from typing import List, Dict, Optional

try:
    import ollama
except ImportError:
    ollama = None

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')
log = logging.getLogger(__name__)

def extract_code_from_file(file_path: Path) -> str:
    """Extract all top-level class/function definitions as one combined string."""
    try:
        source = file_path.read_text(encoding='utf-8')
        tree = ast.parse(source)
    except Exception as e:
        log.warning(f"Skipping {file_path}: {e}")
        return ""

    code_blocks = []
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            try:
                code = ast.unparse(node)
                code_blocks.append(code.strip())
            except Exception as e:
                log.warning(f"Failed to unparse node in {file_path}: {e}")
    return '\n\n'.join(code_blocks)

def enhance_with_ollama(code: str, model: str = 'codellama', retries: int = 3, delay: float = 2.0) -> Optional[str]:
    if not ollama:
        raise RuntimeError("The `ollama` Python package is not installed.")


    for attempt in range(retries):
        try:
            # response = ollama.chat(model=model, messages=[{"role": "user", "content": prompt}])
            response = ollama.chat(
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
            return response['message']['content']
        except Exception as e:
            log.warning(f"Ollama error (attempt {attempt+1}/{retries}): {e}")
            time.sleep(delay * (2 ** attempt))
    return None

def parse_pattern_from_path(path: Path) -> Optional[str]:
    parts = path.parts
    for part in parts:
        if part.lower() in {'singleton', 'factory', 'builder', 'adapter', 'observer', 'decorator', 'strategy', 'command', 'facade'}:
            return part.capitalize()
    return None

def write_chunk(output_dir: Path, metadata: Dict[str, str], original_code: str, enhanced: Optional[str], keep_original: bool):
    chunk_path = output_dir / metadata['filename']

    with open(chunk_path, "w", encoding="utf-8") as f:
        f.write("---\n")
        for key, value in metadata.items():
            if key != "filename":
                f.write(f"{key}: {value}\n")
        f.write("---\n\n")

        if keep_original:
            f.write("```python\n" + original_code.strip() + "\n```\n\n")

        if enhanced:
            f.write("---\n\n" + enhanced.strip() + "\n")

def clean_and_chunk_repo(source_dir, output_dir, enhance=False, keep_original=False, skip_enhanced=False, model="codellama"):
    source_dir = Path(source_dir)
    files_to_process = []

    if source_dir.is_file() and source_dir.suffix == ".py":
        files_to_process = [source_dir]
        use_rel_path = False
    else:
        files_to_process = list(source_dir.rglob("*.py"))
        use_rel_path = True


    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    count = 0

    for file_path in files_to_process:
        print(f"🔍 Processing {file_path}")
        
        if use_rel_path:
            rel_path = file_path.relative_to(source_dir)
        else:
            rel_path = file_path.name  # just the filename

        base_name = (
            rel_path.with_suffix('').as_posix().replace('/', '_').replace('\\', '_')
            if isinstance(rel_path, Path)
            else Path(rel_path).stem
        )
        pattern = parse_pattern_from_path(file_path)

        code_block = extract_code_from_file(file_path)
        if not code_block.strip():
            continue

        chunk_filename = f"{base_name}.md"
        chunk_file = output_dir / chunk_filename

        if skip_enhanced and chunk_file.exists():
            if "## Summary" in chunk_file.read_text(encoding="utf-8"):
                log.info(f"Skipping already enhanced: {chunk_filename}")
                continue

        enhanced = enhance_with_ollama(code_block, model=model) if enhance else None

        metadata = {
            "file": str(rel_path),
            "chunk": base_name,
            "filename": chunk_filename
        }
        if pattern:
            metadata["pattern"] = pattern

        write_chunk(output_dir, metadata, code_block, enhanced, keep_original)
        count += 1

    log.info(f"\n✅ {count} chunks written to: {output_dir.resolve()} (Enhance: {enhance}, Keep original: {keep_original})")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Chunk and optionally enhance Python files for RAG ingestion.")
    parser.add_argument("source", help="Path to the Python project directory or single file")
    parser.add_argument("output", help="Directory to write Markdown chunks")
    parser.add_argument("--enhance", action="store_true", help="Use Ollama to add docstrings and summaries")
    parser.add_argument("--model", default="pattern-rag-gen:latest", help="Ollama model name (default: codellama)")
    parser.add_argument("--keep-original", action="store_true", help="Include the original code in the output")
    parser.add_argument("--skip-enhanced", action="store_true", help="Skip files already enhanced with a summary")

    args = parser.parse_args()
    clean_and_chunk_repo(
        args.source,
        args.output,
        enhance=args.enhance,
        keep_original=args.keep_original,
        skip_enhanced=args.skip_enhanced,
        model=args.model
    )
