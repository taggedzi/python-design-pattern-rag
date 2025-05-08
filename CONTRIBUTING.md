# 🛠 Contributing to python-design-pattern-rag

We welcome contributions that improve this project’s educational value, pattern coverage, and RAG integration. This guide explains how to get your environment set up and how to add or update pattern files.

---

## 🧰 Developer Setup

1. **Install Python 3.10+**
   [Download Python](https://www.python.org/downloads/) if you haven't already.

2. **Install Ollama (for local LLMs)**
   Visit [ollama.com/download](https://ollama.com/download) to install Ollama for your platform.

3. **Clone the Repository**

   ```bash
   git clone https://github.com/taggedzi/python-design-pattern-rag.git
   cd python-design-pattern-rag
   ```

4. **Initialize the Virtual Environment**

   ```bash
   invoke venv
   ```

   This command sets up the virtual environment, installs dependencies, and prepares the CLI commands.

---

## ➕ Adding a New Pattern

1. **Create Your Pattern File**
   Add the new pattern implementation under the appropriate folder in `patterns/`:

   * `patterns/creational/`
   * `patterns/structural/`
   * `patterns/behavioral/`

2. **Generate Lesson and Chunk Files**
   After adding your pattern:

   ```bash
   invoke build-all
   ```

   This will generate:

   * Lesson markdown in `docs/`
   * Chunk markdown in `chunks/`
   * An updated `summary_index.json`

3. **Note:**
   The generation scripts skip files that already exist. To regenerate a specific file, delete it manually before re-running `invoke build-all`.

4. **Edit and Refine**
   Once generated, edit the lesson or chunk files to:

   * Fix typos or formatting
   * Add extra examples or links
   * Improve clarity for learners or RAG usage

---

## 🔧 Build Commands

* `invoke build-lessons` – Regenerates lessons in `docs/`
* `invoke build-chunks` – Regenerates chunk files for RAG
* `invoke build-all` – Runs both and updates the summary index

---

## 🙏 Acknowledgments

This project is made possible with help from:

* [Ollama](https://ollama.com)
* [Falcon 3](https://ollama.com/library/falcon3) by TII
* [DeepSeek Coder](https://ollama.com/library/deepseek-coder) by DeepSeek

---

## 📄 License

This project is licensed under the **MIT License**. See [LICENSE](./LICENSE) for details.
