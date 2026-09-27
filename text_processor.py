import re


def clean_text(text):
    """
    Cleans up messy text:
    - Removes extra blank lines
    - Removes weird multiple spaces
    - Strips leading/trailing whitespace
    """
    # Replace multiple newlines with a single one
    text = re.sub(r'\n\s*\n', '\n', text)
    
    # Replace multiple spaces with a single space
    text = re.sub(r' +', ' ', text)
    
    # Remove leading/trailing whitespace on each line
    lines = [line.strip() for line in text.split('\n')]
    text = '\n'.join(lines)
    
    return text.strip()


def chunk_text(text, chunk_size=800):
    """
    Splits text into smaller chunks (groups of words), 
    so the AI summarizer can handle them one at a time.
    
    chunk_size = how many words go in each chunk.
    """
    words = text.split()
    chunks = []
    
    for i in range(0, len(words), chunk_size):
        chunk = ' '.join(words[i:i + chunk_size])
        chunks.append(chunk)
    
    return chunks


# This part only runs if you run this file directly (for testing)
if __name__ == "__main__":
    from pdf_processor import extract_text_from_pdf
    
    test_pdf_path = "data/sample_cases/sample.pdf"
    raw_text, pages = extract_text_from_pdf(test_pdf_path)
    
    cleaned = clean_text(raw_text)
    chunks = chunk_text(cleaned)
    
    print(f"✅ Cleaned text length: {len(cleaned)} characters")
    print(f"✅ Split into {len(chunks)} chunks")
    print("\nFirst chunk preview:\n")
    print(chunks[0][:500])