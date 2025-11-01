from transformers import pipeline

# Load the model once at startup
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def generate_summary(text: str) -> str:
    """
    Generate a concise summary for the provided text using a pre-trained
    BART model. Automatically adjusts the summary length based on input size
    to prevent overly long or short outputs.
    """
    # Estimate input length by word count
    input_length = len(text.split())

    # Adaptive scaling logic with a higher ceiling
    if input_length < 50:
        max_len = 60
        min_len = 20
    elif input_length < 200:
        max_len = 160
        min_len = 40
    elif input_length < 400:
        max_len = 220
        min_len = 80
    else:
        max_len = 300
        min_len = 100

    # Generate summary
    result = summarizer(
        text, 
        max_length=max_len, 
        min_length=min_len, 
        do_sample=False,
        truncation=True
    )

    return result[0]['summary_text']