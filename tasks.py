"""The task file for the proect, to be used by invoke"""
# pylint: disable=line-too-long
import logging
from pathlib import Path
from invoke import task

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s: %(message)s')

@task
def venv(c):
    """Create virtual environment and install dependencies."""
    logging.info("🟢 Starting to create the working virtual environment...")
    if not Path("venv").exists():
        c.run("python -m venv venv")
        logging.info("  ✅ Virtual environment created successfully!")
    else:
        logging.info("  ⏭️  Virtual environment already exists, skipping creation.")

    logging.info("  📥 Starting to install dependencies...")
    c.run(r".\\venv\\Scripts\\pip install -r requirements.txt")
    logging.info("  ✅ Dependencies installed successfully!")

@task
def setup_ollama(c):
    """Setup Ollama environment."""
    create_rag_model(c)
    create_lessons_model(c)

@task
def create_rag_model(c):
    """Create a custom Ollama model."""
    logging.info("📥 Downloading model for rag generation...")
    c.run("ollama pull deepseek-coder:6.7b")
    logging.info("✅ Model downloaded successfully!")

    logging.info("🛠️ Starting to create the custom model...")
    c.run("ollama create pattern-rag-gen -f ollama/pattern-rag-gen.Modelfile")
    logging.info("✅ Custom model created successfully!")

@task
def create_lessons_model(c):
    """Create a custom Ollama model."""
    logging.info("📥 Downloading model for lesson creation...")
    c.run("ollama pull falcon3:7b")
    logging.info("✅ Model downloaded successfully!")

    logging.info("🛠️ Starting to create the custom model...")
    c.run("ollama create lesson-planner -f ollama/lesson-planner.Modelfile")
    logging.info("✅ Custom model created successfully!")

@task
def build_chunks(c):
    """Run chunk_all_patterns script."""
    logging.info("🧩 Starting to chunk all patterns...")
    c.run(r".\\venv\\Scripts\\python scripts/rag_chunker.py --source patterns --output chunks")
    logging.info("✅ Chunks generated successfully!")

@task
def build_lessons(c, model="lesson-planner:latest"):
    """Generate Markdown lessons."""
    logging.info("📚 Starting to generate lessons...")
    c.run(rf".\\venv\\Scripts\\python scripts/generate_lessons.py --source patterns --output docs --model {model}")
    logging.info("✅ Lessons generated successfully!")
    build_doc_index(c)

@task
def build_search_index(c):
    """Generate summary index."""
    logging.info("🟢 Starting to generate summary index...")
    c.run(r".\\venv\\Scripts\\python scripts/summary_index_generator.py chunks/")
    logging.info("✅ Summary index generated successfully!")

@task
def build_doc_index(c):
    """Generate the index.md file for the docs folder."""
    logging.info("🟢 Starting to generate docs index...")
    c.run(r".\\venv\\Scripts\\python scripts/build_doc_index.py --docs docs --output index.md")
    logging.info("✅ Docs index generated successfully!")

@task
def build_all(c):
    """Run the build pipeline."""
    build_chunks(c)
    build_search_index(c)
    build_lessons(c)

@task
def full(c):
    """Run the full pipeline."""
    venv(c)
    setup_ollama(c)
    build_all(c)
