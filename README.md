# 🧠 SummarySense API – Text Summarization

A lightweight **FastAPI microservice** that takes long text (articles, reviews, transcripts) and returns concise summaries using Hugging Face’s transformers library.

---

## 🧩 Project Overview

SummarySense provides on-demand text summarization for news articles, transcripts, reviews, and long documents.  
It leverages the **facebook/bart-large-cnn** model to generate clear, concise summaries suitable for downstream NLP or content analysis tasks.

---

## 🧠 Tech Stack

| Component     | Technology                                             |
| ------------- | ------------------------------------------------------ |
| Language      | 🤗 Hugging Face Transformers (facebook/bart-large-cnn) |
| Framework     | FastAPI                                                |
| Serving       | Uvicorn                                                |
| Preprocessing | Tokenizer truncation & dynamic summary length          |
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

## 🚀 Running Locally

1. Create and activate your virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Start the API

```bash
uvicorn app:app --reload
```

4. Access interactive docs

```arduino
http://127.0.0.1:8000/docs
```

---

## 🔗 Available API Endpoints

| Endpoint     | Method | Description                                |
| ------------ | ------ | ------------------------------------------ |
| `/summarize` | POST   | Generate a concise summary from input text |
| `/health`    | GET    | Check model and API readiness              |

### Example Request (via curl)

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

## 🛳️ Docker Deployment

### 🧩 Build the Docker Image

```bash
docker build -t summarysense-api .
```

### ▶️ Run the Container Locally

```bash
docker run -d -p 8000:8000 --name summarysense summarysense-api
```

- Verify it’s running:

```bash
docker ps
```

```nginx
CONTAINER ID   IMAGE              COMMAND                  STATUS         PORTS                    NAMES
xxxxxx         summarysense-api   "uvicorn app:app --h…"   Up 5 seconds   0.0.0.0:8000->8000/tcp   summarysense

```

### 🌐 Test the API

```bash
curl -X POST "http://127.0.0.1:8000/summarize" \
     -H "Content-Type: application/json" \
     -d '{"text": "Artificial intelligence has transformed industries around the world. From healthcare and finance to education and entertainment, AI-driven systems are improving efficiency and creating new possibilities for innovation. However, as AI continues to evolve, questions about ethics, transparency, and job displacement remain a major focus for researchers and policymakers."}'
```

- Response

```json
{
  "summary": "AI is transforming industries and improving efficiency, though ethical and employment concerns remain key research areas."
}
```

### 🧹 Stop & Clean Up

```bash
docker stop summarysense && docker rm summarysense
```

### ☁️ Deploy to AWS ECS (Optional)

1. Tag and push your image to Amazon ECR:

```bash
docker tag summarysense-api:latest <your-account-id>.dkr.ecr.<region>.amazonaws.com/summarysense-api:latest
docker push <your-account-id>.dkr.ecr.<region>.amazonaws.com/summarysense-api:latest
```

2. Deploy to ECS using your preferred launch type (Fargate or EC2).

- Your FastAPI summarization microservice will then be accessible via a public ECS endpoint for real-time summarization.

### ✅ **What This Adds**

- Step-by-step **local Docker usage** instructions.
- Clean ECS push command examples for your AWS workflow.
- A **realistic example response** to showcase model output for GitHub viewers.

---

## 🧩 Notes

- The summarization model automatically adjusts max_length based on input size.

- For production, pin dependency versions and build the container image for deployment to ECS or another cloud service.

---

## 📈 Current Progress

- ✅ Project setup

- ✅ Local FastAPI app running and tested

- ✅ Adaptive summarization logic implemented

- [ ] Add logging, /logs, /health, and /info endpoints

- ✅ Containerize with Docker

- [ ] Deploy to AWS ECS

---

👨‍💻 Author

- Kevin Woods
- Applied ML Engineer | AWS Certified AI Practitioner | AWS Machine Learning Certified Engineer – Associate
- 🔗 GitHub: woodskevinj
