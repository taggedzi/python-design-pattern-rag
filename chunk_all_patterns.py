
import subprocess
import sys
from pathlib import Path
import shutil
import time
import datetime

source_dir = Path("patterns")
chunk_dir = Path("docs")
model = "pattern-rag-gen:latest"
index_file = Path("summary_index.json")
log_file = Path("failed_chunks.log")

print("Using Python executable:", sys.executable)

# Clean chunks directory
if chunk_dir.exists():
    print("🧹 Removing old chunks...")
    shutil.rmtree(chunk_dir)
chunk_dir.mkdir(parents=True, exist_ok=True)

# Reset failure log
log_file.write_text("")

# Collect .py files to process
py_files = sorted(source_dir.rglob("*.py"))
remaining = py_files.copy()
max_retries = 3

print(f"📦 Found {len(py_files)} Python files to process.")

while remaining:
    file = remaining.pop(0)
    rel_file = file.relative_to(source_dir)
    chunk_name = rel_file.as_posix().replace("/", "_").replace(".py", ".md")
    chunk_path = chunk_dir / chunk_name

    attempt = 1
    while attempt <= max_retries:
        print(f"🔁 [{attempt}/{max_retries}] Processing {rel_file}...")

        # Run rag_chunker.py with a single file source
        result = subprocess.run([
            sys.executable,
            "rag_chunker.py",
            str(file),
            str(chunk_dir),
            "--enhance",
            "--model", model
        ], check=False)

        if result.returncode != 0:
            print(f"❌ Chunker returned error for {rel_file}")
        elif chunk_path.exists():
            content = chunk_path.read_text(encoding="utf-8")
            if "```python" in content and "Summary:" in content and "Docstrings:" in content:
                print(f"✅ Success: {rel_file}")
                break
            else:
                print(f"⚠️  Incomplete content for {rel_file}")
                chunk_path.unlink(missing_ok=True)
        else:
            print(f"⚠️  Chunk file not created for {rel_file}")

        attempt += 1
        time.sleep(1)
    else:
        msg = f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S} - Failed to chunk: {rel_file}\n"
        log_file.write_text(log_file.read_text() + msg)
        print(f"🚨 Gave up on {rel_file}, logged failure.")

# Generate summary index
print("🗂 Generating summary index...")
index_result = subprocess.run([
    sys.executable,
    "summary_index_generator.py",
    str(chunk_dir),
    str(index_file)
], check=False)
if index_result.returncode == 0:
    print("✅ Summary index created successfully!")
else:
    print("❌ Failed to create summary index.")
