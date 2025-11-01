# 🧠 SummarySense API – Real-Time Sentiment Analysis

A lightweight **FastAPI microservice** that takes long text (articles, reviews, transcripts) and returns concise summaries using Hugging Face’s transformers library.

---

## 🧩 Project Overview

A lightweight **FastAPI microservice** that takes long text (articles, reviews, transcripts) and returns concise summaries using Hugging Face’s transformers library.

## 🧠 Tech Stack

| Component     | Technology                                             |
| ------------- | ------------------------------------------------------ |
| Language      | 🤗 Hugging Face Transformers (facebook/bart-large-cnn) |
| Framework     | FastAPI                                                |
| Serving       | Uvicorn                                                |
| Preprocessing | Tokenizer truncation & padding                         |
| Deployment    | Docker / AWS ECS (optional)                            |

---

## 📂 Project Structure

```css
summarysense-api/
├── app.py
├── src/
│   ├── __init__.py
│   └── summarizer.py
├── requirements.txt
├── README.md
├── Dockerfile
├── .dockerignore
└── .gitignore

```

---

## 🔗 API Endpoints

```bash
curl -X POST "http://127.0.0.1:8000/summarize" \
     -H "Content-Type: application/json" \
     -d '{"text": "Large block of text to summarize..."}'
```

- Response:

```json
{
  "summary": "Concise version of the original text."
}
```

---
