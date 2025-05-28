from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM

# Load model once at startup
model_name = "facebook/bart-large-cnn"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

summarizer = pipeline("summarization", model=model, tokenizer=tokenizer)


def summarize_text(text: str) -> str:
    """
    Summarize the given input text using a pre-trained transformer model.

    Args:
        text (str): The input text to be summarized.

    Returns:
        str: A summary of the input text.
    """
    if not text.strip():
        return "⚠️ No text provided for summarization."

    # Truncate to prevent model token limit issues
    max_input_length = 1024
    inputs = tokenizer.encode(
        text, return_tensors="pt", max_length=max_input_length, truncation=True
    )

    summary_ids = model.generate(
        inputs, max_length=150, min_length=30, length_penalty=2.0, num_beams=4
    )
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary
