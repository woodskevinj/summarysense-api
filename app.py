from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
from src.summarizer import generate_summary

app = FastAPI(
    title="SummarySense API", 
    version="1.0",
    description="Lightweight text summarization API using Hugging Face Transformers."
    )

# Store logs in memory (simple runtime storage)
summary_logs = []

class TextRequest(BaseModel):
    text: str

@app.get("/health")
def health_check():
    return {"status": "ok", "model": "facebook/bart-large-cnn"}

@app.get("/info")
def model_info():
    """Return model and app metadata."""
    return {
        "service": "SummarySense API",
        "version": "1.1",
        "model": "facebook/bart-larg-cnn",
        "framework": "FastAPI",
        "description": "Lightweight summarization microservice using Hugging Face Transformers."
    }

@app.post("/summarize")
def summarize_text(request: TextRequest):
    text = request.text.strip()
    if not text:
        raise HTTPException(status_code=400, detail="Input text cannont be empty.")
    summary = generate_summary(text)

    # Log request and response
    summary_logs.append({
        "timestamp": datetime.utcnow().isoformat(),
        "input_length": len(text.split()),
        "summary_length": len(summary.split()),
        "input": text[:200] + ("..." if len(text) > 200 else ""),
        "summary": summary
    })

    return {"summary": summary}

@app.get("/logs")
def get_logs(limit: int = 10):
    """Return the most recent summarization logs."""
    return summary_logs[-limit:]