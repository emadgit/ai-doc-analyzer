# 📄 AI Document Analyzer

This is a full-stack prototype application that automates the analysis and summarization of textual documents. Built with FastAPI and HuggingFace Transformers, it allows users to paste text or upload `.txt` files, ask natural language questions, and receive summaries via a browser-based UI.

This app was designed to work with academic documents similar to those in the [`ccdv/arxiv-summarization`](https://huggingface.co/datasets/ccdv/arxiv-summarization) dataset. A pre-trained summarization model (BART) was used due to time constraints, but the system is compatible with documents from this dataset.

---

## 🚀 How to Run

### Build the Docker Image
```bash
docker build -t ai-doc-analyzer .
```

### Start the Web App
```bash
docker run -p 8080:8080 ai-doc-analyzer
```

Then open your browser and visit: [http://localhost:8080](http://localhost:8080)

---

## 🧪 How to Run Tests

Make sure you already build the image, then run unit & integration tests with:

```bash
docker run ai-doc-analyzer python /home/src/tests/run_tests.py
```

---

## 🧠 Features

- Upload or paste plain text documents (e.g., scientific abstracts or articles).
- The document is stored in context for follow-up analysis or summarization.
- Ask natural language questions based on the uploaded/pasted document.
- Get AI-generated summaries using a pre-trained LLM (`facebook/bart-large-cnn`).
- Functional browser UI with chat-style history and clear error messages.
- No environment variables or API keys required — runs locally in Docker.

---

## 🏗️ Project Structure

```
Dockerfile
README.md
home/src/
├── app.py             # FastAPI backend
├── summarizer.py      # Summarization logic using HuggingFace
├── ui.html            # Browser-based frontend (HTMX)
├── tests/
│   └── run_tests.py   # Test suite
└── README.md          # This file
```

---

## 📌 Design Notes

- **Cost**: Fully self-contained. No API keys or cloud calls.
- **Stability**: Designed for 100+ queries without crash, tested locally.

---

## 📚 Dataset Used

This app was inspired by the `ccdv/arxiv-summarization` dataset available on HuggingFace. In a production version, training a custom model on that dataset is recommended for improved results.

---

## 🛠️ Extensibility

- Replace `facebook/bart-large-cnn` with a fine-tuned model for domain-specific summaries.
- Add authentication or analytics with minimal changes.
- Swap HTMX for React or Vue if needed.

---

## 🔓 License

This project is intended for demonstration only.
