import streamlit as st
import re
from collections import Counter
import time

# Function to apply themes using CSS
def apply_theme(theme):
    if theme == "Dark 🌙":
        st.markdown(
            """
            <style>
                body {
                    background-color: #1e1e1e;
                    color: white;
                }
                .hover-box:hover {
                    background-color: #444;
                    border-radius: 8px;
                    padding: 5px;
                    transition: 0.3s;
                }
            </style>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            """
            <style>
                body {
                    background-color: white;
                    color: black;
                }
                .hover-box:hover {
                    background-color: #f0f2f6;
                    border-radius: 8px;
                    padding: 5px;
                    transition: 0.3s;
                }
            </style>
            """,
            unsafe_allow_html=True
        )

# Sidebar Theme Selection
st.sidebar.title("⚙️ Settings")
theme = st.sidebar.radio("Select Theme:", ["Light 🌞", "Dark 🌙"])
apply_theme(theme)  # Apply selected theme

# Main Title
st.title("📝 Text Analyzer")

# User Input
user_text = st.text_area("Enter your text here:", height=200)

if st.button("Analyze 🚀"):
    start_time = time.time()
    
    if user_text.strip():
        # Word Count
        words = re.findall(r'\b\w+\b', user_text)
        word_count = len(words)

        # Character Count (excluding spaces)
        char_count = len(user_text.replace(" ", ""))

        # Sentence Count
        sentences = re.split(r'[.!?]', user_text)
        sentences = [s.strip() for s in sentences if s.strip()]
        sentence_count = len(sentences)

        # Most Common Words
        word_freq = Counter(words)
        most_common = word_freq.most_common(5)

        # Average Word Length
        avg_word_length = round(sum(len(word) for word in words) / max(len(words), 1), 2)

        # Reading Time (Assume 200 words per minute)
        reading_time = round(word_count / 200, 2)

        # Display Results
        st.subheader("🔍 Analysis Results")
        col1, col2, col3 = st.columns(3)
        col1.metric("📌 Total Words", word_count)
        col2.metric("📌 Total Characters", char_count)
        col3.metric("📌 Total Sentences", sentence_count)

        st.subheader("📊 Additional Insights")
        st.write(f"📝 **Average Word Length:** {avg_word_length} characters")
        st.write(f"⏳ **Estimated Reading Time:** {reading_time} minutes")

        st.subheader("📊 Most Common Words")
        for word, freq in most_common:
            st.markdown(f"<div class='hover-box'>🔹 **{word}**: {freq} times</div>", unsafe_allow_html=True)

        # Execution Time
        exec_time = round(time.time() - start_time, 3)
        st.write(f"⏱️ **Analysis Completed in** {exec_time} seconds")

        # Download Button
        result = f"Total Words: {word_count}\nTotal Characters: {char_count}\nTotal Sentences: {sentence_count}\nAverage Word Length: {avg_word_length}\nEstimated Reading Time: {reading_time} mins\nMost Common Words: {most_common}"
        st.download_button("📥 Download Report", result, "analysis.txt")
    else:
        st.warning("⚠️ Please enter some text to analyze!")
