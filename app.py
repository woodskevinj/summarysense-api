from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.summarizer import generate_summary

app = FastAPI(title="SummarySense API", version="1.0")

class TextRequest(BaseModel):
    text: str

@app.get("/health")
def health_check():
    return {"status": "ok", "model": "facebook/bart-large-cnn"}

@app.post("/summarize")
def summarize_text(request: TextRequest):
    text = request.text.strip()
    if not text:
        raise HTTPException(status_code=400, detail="Input text cannont be empty.")
    summary = generate_summary(text)
    return {"summary": summary}