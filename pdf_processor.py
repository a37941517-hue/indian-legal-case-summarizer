import pdfplumber

def extract_text_from_pdf(pdf_path):
    """
    Opens a PDF file and pulls out all the readable text.
    Returns the full text as one string, plus the number of pages.
    """
    full_text = ""
    
    with pdfplumber.open(pdf_path) as pdf:
        num_pages = len(pdf.pages)
        
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:  # only add if the page actually has text
                full_text += page_text + "\n"
    
    return full_text, num_pages


def is_scanned_pdf(text):
    """
    Checks if the PDF was basically empty of text (likely a scanned image, not real text).
    Returns True if we think it's a scanned PDF.
    """
    if text.strip() == "":
        return True
    return False


# This part only runs if you run this file directly (for testing)
if __name__ == "__main__":
    test_pdf_path = "data/sample_cases/sample.pdf"  # change this to your actual file
    text, pages = extract_text_from_pdf(test_pdf_path)
    
    if is_scanned_pdf(text):
        print("⚠️ This looks like a scanned PDF with no readable text.")
    else:
        print(f"✅ Extracted text from {pages} pages.")
        print("First 500 characters:\n")
        print(text[:500])