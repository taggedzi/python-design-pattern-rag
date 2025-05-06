![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
![Made for RAG](https://img.shields.io/badge/RAG-Ready-blueviolet)
![Powered by Ollama](https://img.shields.io/badge/Ollama-Compatible-blue)
![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue)
![Built with ❤️ by Matthew Craig](https://img.shields.io/badge/built%20with-%E2%9D%A4%EF%B8%8F%20by%20Matthew%20Craig-orange)

# 🧠 Python Design Patterns for RAG Systems

This repository contains a structured, AI-enhanced collection of Python code examples for major software design patterns — formatted and optimized for use in **Retrieval-Augmented Generation (RAG)** systems, such as those powered by **Open WebUI + Ollama**.

All pattern implementations have been:
- Cleaned and normalized
- Chunked into single-file Markdown documents
- Optionally enriched with **Codellama-based docstrings and summaries**
- Indexed into a machine- and human-readable `summary_index.json`

---

## 📦 Project Structure

```
python-design-pattern-rag/
├── chunks/                  # All pattern code chunks in Markdown format
│   ├── builder_Builder.md
│   ├── factory_SimpleFactory.md
│   └── ...
├── summary_index.json      # Indexed metadata + summaries for each chunk
├── rag_chunker.py          # Script to chunk + enhance Python source files
├── summary_index_generator.py # Script to extract summary metadata from chunks
└── README.md
```

---

## 💡 Features

- ✂️ **File-Level Chunking**: Related classes/functions in each `.py` file are preserved as a single chunk
- 🧠 **Ollama Integration**: Enhancements use [Codellama](https://ollama.com/library/codellama) or other local models to add docstrings + summaries
- 🗃️ **Front Matter Metadata**: Every chunk includes pattern name, file source, and identifiers for easy indexing
- 🔍 **Summary Index**: Machine-readable JSON index to power GUIs or search

---

## 🛠️ How to Use in Open WebUI + Ollama

### 1. **Prepare Your Knowledge Base**

In Open WebUI:
- Go to the **"Knowledge"** tab
- Click **"New Knowledge Base"**
- Choose **Folder** and upload the `chunks/` directory

### 2. **Query with Context Awareness**

Ask things like:
```text
How do I implement the Builder pattern in Python?
What’s the difference between Singleton and Borg patterns?
Show me an example of the Strategy pattern.
```
Your RAG system will retrieve context-rich, formatted answers from these enhanced documents.

### 3. **Search or Visualize with summary_index.json**
Use the `summary_index.json` to:
- Build UIs with sidebar navigation
- Search patterns by type or file
- Feed summaries into tooltips or documentation

---

## 🚀 Scripts

### `rag_chunker.py`
- Chunk Python files into `.md`
- Optionally enhance using a local Ollama model

**Usage:**
```bash
python rag_chunker.py ./source-code ./chunks --enhance --keep-original
```

### `summary_index_generator.py`
- Generate the `summary_index.json` from your `.md` chunks

**Usage:**
```bash
python summary_index_generator.py ./chunks ./summary_index.json
```

---

## 🔄 Supported Patterns (Examples)

- ✅ Singleton
- ✅ Factory
- ✅ Builder
- ✅ Strategy
- ✅ Observer
- ✅ Decorator
- ✅ Adapter
- ✅ Command
- ✅ Facade

> New patterns can be added by running `rag_chunker.py` on new source files.

---

## 📥 Contributing

Contributions are welcome! You can:
- Add new design pattern examples
- Improve docstrings or summaries
- Enhance scripts or tooling

Open issues or pull requests for improvements.

---

## 🙏 Acknowledgments

This project was created and maintained by Matthew Craig with assistance from OpenAI's ChatGPT (powered by GPT-4). Contributions from the AI included scaffolding, documentation, and refinement recommendations.

This project also relies on:
- [Ollama](https://ollama.com) for running local LLMs
- [Code Llama](https://ollama.com/library/codellama) by Meta for AI-based docstring and summary generation with assistance from OpenAI's ChatGPT (powered by GPT-4). Contributions from the AI included scaffolding, documentation, and refinement recommendations.

## 📄 License

This project is licensed under the **MIT License**. See [LICENSE](./LICENSE) for details.
