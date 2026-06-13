import streamlit as st
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer

def summarize_article(article, num_sentences=5):

    parser = PlaintextParser.from_string(
        article,
        Tokenizer("english")
    )

    summarizer = TextRankSummarizer()

    summary = summarizer(
        parser.document,
        num_sentences
    )

    return " ".join(
        str(sentence)
        for sentence in summary
    )

st.set_page_config(
    page_title="News Article Summarizer",
    page_icon="📰"
)

st.title("📰 News Article Summarizer")

article = st.text_area(
    "Paste News Article",
    height=300
)

num_sentences = st.slider(
    "Number of Summary Sentences",
    min_value=1,
    max_value=10,
    value=5
)

if st.button("Generate Summary"):

    if article.strip():

        summary = summarize_article(
            article,
            num_sentences
        )

        st.subheader("Generated Summary")

        st.success(summary)

    else:
        st.warning(
            "Please enter a news article."
        )