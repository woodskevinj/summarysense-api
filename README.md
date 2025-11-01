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

| Endpoint     | Method | Description                                             |
| ------------ | ------ | ------------------------------------------------------- |
| `/summarize` | POST   | Generate a concise summary from input text              |
| `/health`    | GET    | Check model and API readiness                           |
| `/info`      | GET    | Returns app metadata and configuration                  |
| `/logs`      | GET    | Returns the 10 most recent summaries (in-memory buffer) |

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
     -d '{"text": ""Michael Jordan is the greatest basketball player ever. In the history of the NBA. Now, if you aren’t a fan of his personal choices (gambling, his yellow eyes, or his decision to ruin the Charlotte Hornets) or even his perceived lack of social activism (which is fine despite not being true), that’s certainly acceptable, but keep in mind, we know Jordan for one major thing, and that’s basketball. At the game of basketball, there was no one better at the game, and while we sat and tried to compare players of this era to Jordan, there was really nothing to compare. Jordan is head and shoulders above all. There is an argument to be made for Kareem Abdul Jabbar, but as a player who was well over 7 foot, playing on the Los Angeles Lakers during the stacked Showtime era, it is hard to rank Kareem over Jordan. Sure, Kareem had the record for most points ever (now LeBron), as well as leading the league in blocks and 6 MVP awards, but those are stats amassed over a 20 year career compared to a 12 year run in Chicago for Jordan where he amassed 5 MVP awards (should have been 7), 6 Titles and Finals MVPs, and 10 scoring titles, including 7 in a row. Today, we take a moment to look back at the success and the accolades of Jordan to put those talks and debates to rest... or at least attempt to. Let’s take a look at Jordan and his accolades. There are so many to cover, so we’ll cover the most important. Remember that one of the arguments for LeBron being better than Jordan is that he could do more on the court? Well, a smaller sample size was given to the world once we got a glimpse of Jordan running the point, and with that, Jordan would show exactly what he can do, by posting gaudy numbers and leading the Bulls to victories. This is an accolade to me because truth be told, the biggest discussion against Jordan was that perhaps he wasn’t as well rounded as say Magic, LeBron, or some other players. For one, Jordan in his prime was an excellent defender, one of the greatest ever, and that separates him from the pack out the gate, but the fact that Jordan playing point guard led him to a promised land of stats (and more importantly victories) showcases that he could do everything on the court at all times. He would put up 7 straight triple doubles during the 1988-1989 season, earning praise for the Bulls putting the ball in his hands more, which is essentially what they needed to do from the start."}'
```

- Response

```json
{
  "summary": "Michael Jordan is the greatest basketball player ever. In the history of the NBA. There is an argument to be made for Kareem Abdul Jabbar, but as a player who was well over 7 foot, playing on the Los Angeles Lakers during the stacked Showtime era, it is hard to rank Kareem over Jordan. Jordan amassed 5 MVP awards, 6 Titles and Finals MVPs, and 10 scoring titles, including 7 in a row. He would put up 7 straight triple doubles during the 1988-1989 season, earning praise for the Bulls putting the ball in his hands more."
}
```

> _Example text excerpt adapted from [“What Makes Michael Jordan the G.O.A.T.”](https://medium.com/@DARSportsAndMedia/what-makes-michael-jordan-the-g-o-a-t-950e9758c00b) by DARSportsAndMedia on Medium._

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

- ✅ Add logging, /logs, /health, and /info endpoints

- ✅ Containerize with Docker

- [ ] Deploy to AWS ECS (optional)

---

## 🧑‍💻 Developer Corner – Experimenting with Generation Behavior

For developers who want to explore **how temperature and sampling** affect summarization output, you can experiment safely by adjusting the generation parameters below.

This snippet enables _creative summarization mode_, giving you control over the balance between determinism and variation.

```python
result = summarizer(
    text,
    max_length=max_len,
    min_length=min_len,
    do_sample=True,       # Enable sampling
    temperature=0.9,      # Default is 1.0; lower = more focused, higher = more diverse
    top_k=50,             # Consider top 50 tokens for diversity
    top_p=0.95,           # Use nucleus sampling (95% probability mass)
    truncation=True
)
```

### 🔧 Experimenting with Temperature

You can fine-tune generation behavior with temperature adjustments:

- `temperature=0.7` → More focused, less repetition

- `temperature=1.2` → More variation, possibly looser summaries

This is a great way to **tune tone, creativity, and compression** depending on your use case or text domain.

---

👨‍💻 Author

- Kevin Woods
- Applied ML Engineer | AWS Certified AI Practitioner | AWS Machine Learning Certified Engineer – Associate
- 🔗 GitHub: woodskevinj
