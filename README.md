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

```text
python-design-pattern-rag/
├── chunks/                            # All pattern code chunks in Markdown format
│   ├── builder_Builder.md
│   ├── factory_SimpleFactory.md
│   └── ...
├── docs/                              # All pattern code chunks in Markdown format
│   ├── builder_Builder.md
│   ├── factory_SimpleFactory.md
│   ├── index.md
│   └── ...
├── patterns/                          # All pattern code examples
│   ├── creational/                    # Creational patterns (e.g. Builder)
│   |   ├── abstract_factory.py
│   |   ├── builder.py
│   |   └── ...
│   ├── structural/                    # Structural patterns (e.g. Factory)
│   |   ├── adapter.py
│   |   ├── decorator.py
│   |   └── ...
│   └── behavioral/                    # Behavioral patterns (e.g. Observer)
│       ├── observer.py
│       ├── memento.py
│       └── ...
├── ollama/                            # Ollama related files
│       ├── lesson-planner.ModelFile   # Modelfile for Ollama 
│       ├── pattern-rag-gen.ModelFile  # Modelfile for Ollama 
|       └── README.md                  # Instructions on configuration for Ollama
├── summary_index.json                 # Indexed metadata + summaries for each chunk
├── rag_chunker.py                     # Script to chunk + enhance Python source files
├── chunk_all_patterns.py              # Script to chunk all patterns in `patterns/`
├── summary_index_generator.py         # Script to extract summary metadata from chunks
└── README.md
```

---

## 💡 Features

- 🏫 **Generated Examples of Python Patterns**: Each file is a complete example of a python pattern. See the [patterns](patterns/) folder.
- 🏫 **Educational Documentation**: Each python pattern has a generated lesson plan for easy learning and understanding. [Docs](https://taggedzi.github.io/python-design-pattern-rag/)
- 📦 **RAG File Generation**: Files in the `chunks/` are enhanced with docstrings and summaries and formatted to be consumed by RAG systems.
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

> New patterns can be added in the `patterns` folder. Then running `invoke build-all` in the root directory of this repo will generate all the Docs, Chunks, and summary_index.json file. Please note EVERY time you run a build comman it will generate all the docs and chunks from scratch using a local LLM so each time the documents for all files will be slightly different. Please only commit files that are relevant to the pattern you're adding.  Despite the large amount of automation there is still a lot of manual work involved in building the docs and chunks. Any commits that modify all the files will probably be denied.

---

**Everything below here is ONLY needed if you wish to contributed to the project or build the RAG files yourself.**

---

## 📥 Contributing

Contributions are welcome! You can:

- Add new design pattern examples
- Improve docstrings or summaries
- Enhance scripts or tooling

Open issues or pull requests for improvements.

## Setup if you want to contribute or build RAG files yourself

1. Verify you have Python and pip installed. The project runs on python Python 3.10+ and pip. See [Python.org](https://www.python.org/) for installation instructions.

2. Install Ollama and run it locally. Files can be downloaded from [ollama.com](https://ollama.com/download) for thier download options.

3. Use git to clone this repository. `git clone https://github.com/taggedzi/python-design-pattern-rag.git` or download the zip archive and extract it to your desired location.

4. Navigate to the project root directory and run `invoke venv` to setup the virtial environment, pull down dependancies, and get your envionment ready to go.

5. To build ALL all the lessons and index:
   ```bash
      invoke build-lessons
   ```

6. To build all the RAG files:
   ```bash
      invoke build-chunks
   ```

7. To build everything:
   ```bash
      invoke build-all
   ```

## 🙏 Acknowledgments

This project was created and maintained by Matthew Craig (TaggedZi) with assistance from OpenAI's ChatGPT (powered by GPT-4). Contributions from the AI included scaffolding, documentation, and refinement recommendations.

This project also relies on:

- [Ollama](https://ollama.com) for running local LLMs
- [Falcon 3](https://ollama.com/library/falcon3) by [TII](https://www.tii.ae/ai-and-digital-science) for AI-based contributions including scaffolding, documentation, and refinement recommendations.
- [Deepseek Coder](https://ollama.com/library/deepseek-coder) by DeepSeek for AI-based contributsions producing the lesson files.

## 📄 License

This project is licensed under the **MIT License**. See [LICENSE](./LICENSE) for details.
