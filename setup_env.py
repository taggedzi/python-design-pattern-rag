import os
import subprocess
import sys
from pathlib import Path

venv_dir = Path("venv")

# Step 1: Create venv if it doesn't exist
if not venv_dir.exists():
    print("🔧 Creating virtual environment...")
    subprocess.run([sys.executable, "-m", "venv", str(venv_dir)], check=True)
else:
    print("✅ Virtual environment already exists.")

# Step 2: Determine paths to pip and python inside venv
if os.name == "nt":  # Windows
    pip_path = venv_dir / "Scripts" / "pip.exe"
    activate_cmd = venv_dir / "Scripts" / "activate.bat"
else:  # Unix-like
    pip_path = venv_dir / "bin" / "pip"
    activate_cmd = f"source {venv_dir}/bin/activate"

# Step 3: Install requirements
print("📦 Installing dependencies from requirements.txt...")
subprocess.run([str(pip_path), "install", "-r", "requirements.txt"], check=True)

# Step 4: Done
print("✅ Environment is ready!")
print(f"💡 To activate it manually, run:\n  {activate_cmd}")