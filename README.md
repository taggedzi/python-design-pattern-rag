![Made for RAG](https://img.shields.io/badge/RAG-Ready-blueviolet)
![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue)
![Powered by Ollama](https://img.shields.io/badge/Ollama-Compatible-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
![Built with ❤️ by Matthew Craig](https://img.shields.io/badge/built%20with-%E2%9D%A4%EF%B8%8F%20by%20TaggedZi-orange)

# 🧠 Python Design Patterns and RAG files for Retrieval-Augmented Generation (RAG) in other AI systems

This repository contains a structured, AI-enhanced collection of Python code demonstrating the major software design patterns in python.

This project ALSO includes formatted and optimized Markdown files for use in **Retrieval-Augmented Generation (RAG)** systems, such as those powered by **Open WebUI + Ollama** that describes the patterns in a way that is optimized for use in **Retrieval-Augmented Generation (RAG)** systems, such as those powered by **Open WebUI + Ollama**.

All pattern implementations have been:

- Cleaned and normalized and documented with docstrings and comments.
- Chunked into single-file Markdown documents
- Optionally enriched with **AI-based docstrings and summaries**
- Indexed into a machine- and human-readable `summary_index.json`

---

## 📦 Project Structure

```bash
python-design-pattern-rag/
├── chunks/                      # All pattern code chunks in Markdown format
│   ├── builder_Builder.md
│   ├── factory_SimpleFactory.md
│   └── ...
├── patterns/                    # All pattern code examples
│   ├── creational/              # Creational patterns (e.g. Builder)
│   |   ├── abstract_factory.py
│   |   ├── builder.py
│   |   └── ...
│   ├── structural/              # Structural patterns (e.g. Factory)
│   |   ├── adapter.py
│   |   ├── decorator.py
│   |   └── ...
│   └── behavioral/              # Behavioral patterns (e.g. Observer)
│       ├── observer.py
│       ├── memento.py
│       └── ...
├── ollama/                      # Ollama related files
│       ├── ModelFile            # Modelfile for Ollama 
|       └── README.md            # Instructions on configuration for Ollama
├── summary_index.json           # Indexed metadata + summaries for each chunk
├── rag_chunker.py               # Script to chunk + enhance Python source files
├── chunk_all_patterns.py        # Script to chunk all patterns in `patterns/`
├── summary_index_generator.py   # Script to extract summary metadata from chunks
└── README.md
```

---

## 💡 Features

- ✂️ **File-Level Chunking**: Related classes/functions in each `.py` file are preserved as a single chunk
- 🧠 **Ollama Integration**: Enhancements use [Falcon 3](https://ollama.com/library/falcon3) or other local models to add docstrings + summaries
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

**Everything below here is ONLY needed if you wish to contributed to the project or build the RAG files yourself.**

---

## 📥 Contributing

Contributions are welcome! You can:

- Add new design pattern examples
- Improve docstrings or summaries
- Enhance scripts or tooling

Open issues or pull requests for improvements.

## Setup

1. Verify you have Python and pip installed. The project runs on python Python 3.10+ and pip. See [Python.org](https://www.python.org/) for installation instructions.

2. Use git to clone this repository. `git clone https://github.com/taggedzi/python-design-pattern-rag.git` or download the zip archive and extract it to your desired location.

3. Navigate to the project root directory and run `pip install -r requirements.txt`.

4. Install Ollama and run it locally. Files can be downloaded from [ollama.com](https://ollama.com/download) for thier download options.

5. Download the `falcon3:7b` model locally. See [Falcon 3](https://ollama.com/library/falcon3) for more information.

6. Use Ollama to create the custom model locally. See [ollama/README.md](./ollama/README.md) for more information.

7. To build ALL all the Markdown files run:
   ```bash
   python chunk_all_patterns.py
   ```

8. To build a single file run:
   ```bash
    python rag_chunker.py ./patterns/<type>/<pattern>.py chunks --enhance
   ```

---

## 🚀 Scripts

### `rag_chunker.py`

- Chunk Python files into `.md`
- Optionally enhance using a local Ollama model

**Usage:**

```bash
python rag_chunker.py ./patterns/<type>/<pattern>.py ./chunks --enhance
```

For more information on this script, please refer to the source code, or call the script itself with the `--help` option.

### `summary_index_generator.py`

- Generate the `summary_index.json` from your `.md` chunks

**Usage:**

```bash
python summary_index_generator.py ./chunks ./summary_index.json
```

## 🙏 Acknowledgments

This project was created and maintained by Matthew Craig with assistance from OpenAI's ChatGPT (powered by GPT-4). Contributions from the AI included scaffolding, documentation, and refinement recommendations.

This project also relies on:

- [Ollama](https://ollama.com) for running local LLMs
- [Falcon 3](https://ollama.com/library/falcon3) by [TII](https://www.tii.ae/ai-and-digital-science) for AI-based contributions including scaffolding, documentation, and refinement recommendations.

## 📄 License

This project is licensed under the **MIT License**. See [LICENSE](./LICENSE) for details.
