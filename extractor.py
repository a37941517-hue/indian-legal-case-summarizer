import re


def extract_case_number(text):
    """
    Looks for lines like 'CIVIL APPEAL NO. 4779 OF 2019'
    """
    match = re.search(r'(CIVIL|CRIMINAL|WRIT)\s+APPEAL\s+NO\.?\s*[\d]+\s*OF\s*\d{4}', text, re.IGNORECASE)
    if match:
        return match.group(0).strip()
    return "Not found"


def extract_court(text):
    """
    Looks for the court name, e.g. 'IN THE SUPREME COURT OF INDIA'
    """
    match = re.search(r'IN THE (SUPREME COURT OF INDIA|HIGH COURT OF [A-Z\s]+)', text, re.IGNORECASE)
    if match:
        return match.group(0).strip()
    return "Not found"


def extract_bench(text):
    """
    Looks for a line starting with 'Bench:'
    """
    match = re.search(r'Bench:\s*(.+)', text)
    if match:
        return match.group(1).strip()
    return "Not found"


def extract_author(text):
    """
    Looks for a line starting with 'Author:'
    """
    match = re.search(r'Author:\s*(.+)', text)
    if match:
        return match.group(1).strip()
    return "Not found"


def extract_parties(text):
    """
    Looks for a pattern like 'X ...vs... Y' near the top of the judgment,
    which usually shows petitioner and respondent.
    """
    match = re.search(r'([A-Z][A-Za-z\.\s&]+)\s+(?:VERSUS|VS\.?|V\.)\s+([A-Z][A-Za-z\.\s&]+)', text)
    if match:
        petitioner = match.group(1).strip()
        respondent = match.group(2).strip()
        return petitioner, respondent
    return "Not found", "Not found"


def extract_all_fields(text):
    """
    Runs all the extractors and returns everything as one dictionary
    (a labeled box of results, like a form filled in).
    """
    petitioner, respondent = extract_parties(text)
    
    return {
        "case_number": extract_case_number(text),
        "court": extract_court(text),
        "bench": extract_bench(text),
        "author": extract_author(text),
        "petitioner": petitioner,
        "respondent": respondent,
    }


# This part only runs if you run this file directly (for testing)
if __name__ == "__main__":
    from pdf_processor import extract_text_from_pdf
    from text_processor import clean_text
    
    test_pdf_path = "data/sample_cases/sample.pdf"
    raw_text, pages = extract_text_from_pdf(test_pdf_path)
    cleaned = clean_text(raw_text)
    
    fields = extract_all_fields(cleaned)
    
    print("✅ Extracted fields:\n")
    for key, value in fields.items():
        print(f"{key}: {value}")