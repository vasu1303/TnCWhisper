from transformers import pipeline, BartTokenizer
import re


# Load BART model and tokenizer
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
tokenizer = BartTokenizer.from_pretrained("facebook/bart-large-cnn")
max_tokens = 1024  # BART's safe max


def clean_text(text):
    # Replace multiple whitespace characters (spaces, tabs, newlines) with a single space
    return re.sub(r'\s+', ' ', text).strip()


def chunk_text_by_tokens(text, tokenizer, max_tokens=1024):
    
    sentences = re.split(r'(?<=[.!?]) +', text)
    chunks = []
    current_chunk = ""

    for sentence in sentences:
        test_chunk = (current_chunk + " " + sentence).strip() if current_chunk else sentence
        input_ids = tokenizer.encode(test_chunk, add_special_tokens=False)

        if len(input_ids) <= max_tokens:
            current_chunk = test_chunk
        else:
            if current_chunk:
                chunks.append(current_chunk.strip())
            current_chunk = sentence

    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks

def summarization(text):
    text = clean_text(text)
    chunks = chunk_text_by_tokens(text, tokenizer, max_tokens)
    summaries = []

    for i, chunk in enumerate(chunks):
        try:
            prompt = f"Summarize the following Terms and Conditions as concise bullet points:\n{chunk}"
            summary = summarizer(
                prompt,
                max_length=400,
                min_length=60,
                do_sample=False,
                no_repeat_ngram_size=3
            )[0]['summary_text']
            summaries.append(summary)
        except Exception as e:
            print(f"⚠️ Error summarizing chunk {i+1}: {e}")
            continue

    # Post-process: split into sentences and add bullets
    all_text = " ".join(summaries)
    # Split on period, question mark, or exclamation mark followed by space or end of string
    
    sentences = re.split(r'(?<=[.!?])\s+', all_text)
    bullets = [f"- {s.strip()}" for s in sentences if s.strip()]
    return "\n".join(bullets)
