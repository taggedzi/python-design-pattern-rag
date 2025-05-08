# 🧠 Python Design Patterns — Learn & Use with AI

![Made for RAG](https://img.shields.io/badge/RAG-Ready-blueviolet)
![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue)
![Powered by Ollama](https://img.shields.io/badge/Ollama-Compatible-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
![Built with ❤️ by TaggedZi](https://img.shields.io/badge/built%20with-%E2%9D%A4%EF%B8%8F%20by%20TaggedZi-orange)

> 📚 **Looking to learn design patterns in Python?**
> Explore our [docs and lessons](https://taggedzi.github.io/python-design-pattern-rag/) to study and apply design patterns through clear, hands-on examples — perfect for self-paced learning or AI-assisted coding!

---

## 📌 What This Project Does

This repository helps you:

1. **Learn software design patterns in Python** with clean, structured examples.
2. **Use those lessons with LLMs** like ChatGPT, Open WebUI, or Ollama for **Retrieval-Augmented Generation (RAG)** coding workflows.
3. **Leverage preprocessed pattern chunks** and a searchable index to integrate design knowledge directly into AI tooling.

---

## 🏫 Educational Lessons & Docs

Visit our [website](https://taggedzi.github.io/python-design-pattern-rag/) or the [`docs/`](docs/) directory to find:

* Lesson plans and code walkthroughs for each pattern.
* Example-driven explanations optimized for learning and memory.
* Markdown-formatted versions ideal for study or RAG ingestion.

---

## 🔄 RAG-Optimized Content

If you want to integrate pattern knowledge into AI tools:

* Use the `chunks/` directory: preprocessed, docstring-enhanced Markdown files.
* Reference `summary_index.json`: a machine-readable index with metadata and summaries.

These resources are **ready to drop into Open WebUI, Ollama**, or any system that supports knowledge base ingestion.

---

## 🛠 How to Use with Open WebUI + Ollama

### 1. Add to a Knowledge Base

* Open the **"Knowledge"** tab in WebUI.
* Create a new base using the `chunks/` folder.

### 2. Ask Contextual Questions

Use your RAG-enabled system to ask:

```text
How do I implement the Builder pattern in Python?
What's the difference between Singleton and Borg?
Show me a working example of the Strategy pattern.
```

### 3. Use the Index

Use `summary_index.json` to:

* Power UI navigation
* Search by pattern
* Generate dynamic summaries

---

## 📁 Project Structure

```text
python-design-pattern-rag/
├── chunks/              # RAG-optimized pattern files (Markdown)
├── docs/                # Educational lessons and explanations
├── patterns/            # Raw Python implementations of each pattern
├── ollama/              # Ollama-specific configuration (for development)
├── scripts/             # Scripts for building Docs and RAG files (for development)
├── CONTRIBUTING.md      # Instructions and Guidelines for contributing
├── LICENSE              # License information
├── README.md            # Project overview and instructions
├── requirements.txt     # Project dependencies (for development)
├── summary_index.json   # Index of all patterns and their RAG files
└── tasks.py             # Tasks for building the project
```

---

## ✅ Supported Patterns (so far)

* Abstract Factory
* Adapter
* Bridge
* Builder
* Chain of Responsibility
* Command
* Composite
* Decorator
* Facade
* Factory
* Flyweight
* Interpreter
* Memento
* Observer
* Prototype
* Proxy
* Singleton
* State
* Strategy
* Template Method
* Visitor

---

### 👩‍💻 Developers & Contributors

If you’d like to build, extend, or contribute to this project, check out our [Developer Guide](CONTRIBUTING.md) for setup instructions and contribution tips.

---

### 🙏 Acknowledgments

This project was created and maintained by Matthew Craig (TaggedZi) with assistance from OpenAI's ChatGPT (powered by GPT-4). Contributions from the various AIs included scaffolding, documentation, and refinement recommendations.

This project also relies on:

* [Ollama](https://ollama.com) for running local LLMs
* [Falcon 3](https://ollama.com/library/falcon3) by [TII](https://www.tii.ae/ai-and-digital-science) for AI-based contributions including scaffolding, documentation, and refinement recommendations.
* [Deepseek Coder](https://ollama.com/library/deepseek-coder) by DeepSeek for AI-based contributsions producing the lesson files.

---

### 📄 License

This project is licensed under the **MIT License**. See [LICENSE](./LICENSE) for details.
