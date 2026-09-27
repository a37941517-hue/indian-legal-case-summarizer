import streamlit as st
from pdf_processor import extract_text_from_pdf, is_scanned_pdf
from text_processor import clean_text, chunk_text
from summarizer import summarize_full_text
from extractor import extract_all_fields

st.set_page_config(page_title="Indian Legal Case Summarizer", layout="wide")

st.title("⚖️ Indian Legal Case Summarizer")
st.write("Upload a court judgment PDF and get a summary plus key details.")

# File uploader widget - lets the user pick a PDF from their computer
uploaded_file = st.file_uploader("Upload a PDF judgment", type=["pdf"])

if uploaded_file is not None:
    # Save the uploaded file temporarily so our existing functions can open it
    temp_path = "temp_uploaded.pdf"
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    with st.spinner("Reading PDF..."):
        raw_text, num_pages = extract_text_from_pdf(temp_path)

    if is_scanned_pdf(raw_text):
        st.error("⚠️ This looks like a scanned PDF with no readable text. Please upload a text-based PDF.")
    else:
        st.success(f"✅ Extracted text from {num_pages} pages.")

        cleaned = clean_text(raw_text)
        chunks = chunk_text(cleaned)

        # Extracted fields (fast, no AI needed)
        with st.spinner("Extracting case details..."):
            fields = extract_all_fields(cleaned)

        st.subheader("📋 Case Details")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"**Court:** {fields['court']}")
            st.markdown(f"**Case Number:** {fields['case_number']}")
            st.markdown(f"**Bench:** {fields['bench']}")
        with col2:
            st.markdown(f"**Author:** {fields['author']}")
            st.markdown(f"**Petitioner:** {fields['petitioner']}")
            st.markdown(f"**Respondent:** {fields['respondent']}")

        # Summary (slower, uses AI - only runs when button is clicked)
        st.subheader("📝 Summary")
        if st.button("Generate Summary"):
            with st.spinner(f"Summarizing {len(chunks)} chunks... this may take a minute."):
                final_summary = summarize_full_text(chunks)
            st.write(final_summary)