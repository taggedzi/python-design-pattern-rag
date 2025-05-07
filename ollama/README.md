# 🔧 Local Setup for a custom Model in Ollama for Design Pattern RAG

This guide walks you through configuring a custom Ollama model and using it to enhance Python code with docstrings and summaries for use in a Retrieval-Augmented Generation (RAG) pipeline.

---

## 📦 Prerequisites

Before proceeding, ensure the following are installed:

- [Ollama](https://ollama.com/)
- Python 3.10+  
- A virtual environment (via `venv` or `conda`)
- Python dependencies from the project's `requirements.txt`

```bash
# Example setup with venv
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

---

## 🧠 Choose & Download a Model

Download an Ollama-compatible model. After testing several options, we recommend:

```bash
ollama pull falcon3:7b
```

> ✅ Note: `falcon3:7b` strikes a good balance of quality and speed for structured code summarization. It has yeilded the best results after several rounds of testing.

---

## ⚙️ Build a Custom Ollama Model

1. Navigate to the directory containing your `Modelfile`.
2. If you choose a different model, update the `FROM` line in the `Modelfile` accordingly:
   ```dockerfile
   FROM <your-model-here>
   ```

3. Create the custom model:
   ```bash
   ollama create pattern-rag-gen -f Modelfile
   ```

This model will specialize in summarizing and annotating code for the design pattern RAG project.
