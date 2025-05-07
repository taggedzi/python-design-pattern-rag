import subprocess
import sys
from pathlib import Path
import shutil
import time

source_dir = Path("patterns")
chunk_dir = Path("chunks")
model = "pattern-rag-gen:latest"
index_file = Path("summary_index.json")

print("Using Python executable:", sys.executable)

# Clean up old chunks
if chunk_dir.exists():
    print("🧹 Removing old chunks...")
    shutil.rmtree(chunk_dir)
chunk_dir.mkdir(parents=True, exist_ok=True)

print("📦 Chunking and enriching all patterns for RAG...")

# Initial full run to populate all chunks
subprocess.run([
    sys.executable,
    "rag_chunker.py",
    str(source_dir),
    str(chunk_dir),
    "--enhance",
    "--model", model
], check=True)

# Retry logic for missing files
max_retries = 3
retry_count = 0

while retry_count < max_retries:
    missing_files = []

    for path in chunk_dir.glob("*.md"):
        content = path.read_text(encoding="utf-8")
        if "```python" not in content or "Summary:" not in content or "Docstrings:" not in content:
            missing_files.append(path.stem)

    if not missing_files:
        print("✅ All chunks verified: code, summary, and docstrings present.")
        break

    print(f"🔁 Pass {retry_count + 1}: Reprocessing {len(missing_files)} incomplete chunk(s)...")

    for file_stem in missing_files:
        # Remove bad chunk
        bad_chunk = chunk_dir / f"{file_stem}.md"
        if bad_chunk.exists():
            bad_chunk.unlink()

    # Run chunker again on full source directory (it will recreate missing only)
    subprocess.run([
        sys.executable,
        "rag_chunker.py",
        str(source_dir),
        str(chunk_dir),
        "--enhance",
        "--model", model
    ], check=True)

    retry_count += 1
    time.sleep(1)

if retry_count >= max_retries:
    print("⚠️  Some files may still be incomplete after maximum retries.")
    for path in chunk_dir.glob("*.md"):
        content = path.read_text(encoding="utf-8")
        if "```python" not in content or "Summary:" not in content or "Docstrings:" not in content:
            print(" -", path.name)

# Generate summary index
print("🗂 Generating summary index...")
index_result = subprocess.run([
    sys.executable,
    "summary_index_generator.py",
    str(chunk_dir),
    str(index_file)
], check=True)
if index_result.returncode == 0:
    print("✅ Summary index created successfully!")
else:
    print("❌ Failed to create summary index.")
