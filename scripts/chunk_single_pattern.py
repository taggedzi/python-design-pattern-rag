import subprocess
import sys
from pathlib import Path
import shutil
import time
import time
from typing import Optional

from argparse import ArgumentParser

parser = ArgumentParser(description="Chunk and enhance a single Python design pattern file for RAG.")
parser.add_argument("source_file", type=Path, help="Path to the single .py file to process")
parser.add_argument("--model", default="codellama", help="Ollama model to use for enhancement")
parser.add_argument("--retries", type=int, default=3, help="Number of retries if enhancement fails")
args = parser.parse_args()

source_file = args.source_file.resolve()
chunk_dir = Path("chunks")
model = args.model
retries = args.retries

if not source_file.exists():
    print(f"❌ Source file not found: {source_file}")
    sys.exit(1)

# Temp source directory to isolate this file
temp_source_dir = Path(".tmp_single")
temp_source_dir.mkdir(exist_ok=True)
temp_file = temp_source_dir / source_file.name
shutil.copy2(source_file, temp_file)

# Retry loop for enhancement
attempt = 1
while attempt <= retries:
    print(f"🔁 Attempt {attempt} to process {source_file.name}...")

    result = subprocess.run([
        sys.executable,
        "rag_chunker.py",
        str(temp_source_dir),
        str(chunk_dir),
        "--enhance",
        "--model", model
    ], check=False)

    if result.returncode != 0:
        print(f"❌ Chunking failed on attempt {attempt}")
        attempt += 1
        time.sleep(1)
        continue

    # Check generated chunk
    chunk_name = source_file.stem.replace("/", "_").replace("\\", "_") + ".md"
    chunk_path = chunk_dir / chunk_name
    if chunk_path.exists():
        content = chunk_path.read_text(encoding="utf-8")
        if "```python" in content and "Summary:" in content and "Docstrings:" in content:
            print(f"✅ Chunk created and verified: {chunk_path}")
            break
        else:
            print(f"⚠️  Missing required sections in {chunk_path.name}, retrying...")
            chunk_path.unlink()
    else:
        print(f"⚠️  Expected chunk not found: {chunk_name}")

    attempt += 1
    time.sleep(1)
else:
    print(f"❌ Failed to process {source_file.name} after {retries} attempts")

# Clean up temp dir
shutil.rmtree(temp_source_dir)
