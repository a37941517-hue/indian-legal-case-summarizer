import streamlit as st
from transformers import pipeline


@st.cache_resource
def load_summarizer():
    print("Loading AI model... this may take a minute the first time.")

    model = pipeline(
        "summarization",
        model="sshleifer/distilbart-cnn-12-6"
    )

    print("Model loaded!")
    return model


summarizer_model = load_summarizer()


def summarize_chunk(text_chunk):
    """
    Takes one chunk of text and returns a short summary.
    """

    result = summarizer_model(
        text_chunk,
        max_length=130,
        min_length=30,
        do_sample=False,
        truncation=True
    )

    return result[0]["summary_text"]


def summarize_full_text(chunks):

    summaries = []

    for i, chunk in enumerate(chunks):

        print(f"Summarizing chunk {i + 1} of {len(chunks)}...")

        summary = summarize_chunk(chunk)

        summaries.append(summary)

    final_summary = " ".join(summaries)

    return final_summary