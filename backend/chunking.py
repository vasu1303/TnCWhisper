def chunk_text(text, max_words=900):
    import re
    # this regex will split sentences 
    sentences = re.split(r'(?<=[.!?]) +', text)
    chunks = []
    current_chunk = []

    current_len = 0
    for sentence in sentences:
        word_count = len(sentence.split())
        if current_len + word_count <= max_words:
            current_chunk.append(sentence)
            current_len += word_count
        else:
            chunks.append(" ".join(current_chunk))
            current_chunk = [sentence]
            current_len = word_count
    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks
