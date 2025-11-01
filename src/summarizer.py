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

    # Dynamically adjust max_length (cap at 130 tokens)
    # - For short text: shorten summary length
    # - For long text: allow longer summaries
    max_len = min(130, max(30, int(input_length * 0.5)))
    min_len = max(10, int(max_len * 0.3))

    # Generate summary
    result = summarizer(text, max_length=max_len, min_length=min_len, do_sample=False)
    return result[0]['summary_text']