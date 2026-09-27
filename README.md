# Indian Legal Case Summarizer ⚖️

An AI-powered tool that reads Indian court judgment PDFs and produces a short summary along with key structured details (court, case number, bench, author, petitioner, respondent).

## What it does
- Upload a court judgment PDF through a simple web interface
- Extracts the raw text from the PDF
- Cleans and splits the text into manageable chunks
- Uses a Hugging Face summarization model to generate a concise summary
- Extracts structured case details using pattern matching (regex)

## Tech stack
- **Python**
- **Streamlit** – web interface
- **pdfplumber** – PDF text extraction
- **Hugging Face Transformers** (`sshleifer/distilbart-cnn-12-6`) – AI summarization
- **Regex** – structured field extraction

## How to run locally
1. Clone this repository
2. Create a virtual environment: `python -m venv venv`
3. Activate it: `venv\Scripts\activate` (Windows)
4. Install dependencies:
5. Run the app:
## Known limitations
- Petitioner/respondent extraction is pattern-based and may not always correctly identify the parties, especially in complex judgments with multiple case citations
- Only works with text-based PDFs (not scanned image PDFs without OCR)
- Summarization uses a general-purpose model, not one fine-tuned specifically for legal text

## Author
Built as a learning project by a first-time developer, with guidance along the way.
