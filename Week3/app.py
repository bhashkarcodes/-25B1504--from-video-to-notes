import streamlit as st
from summarizer.pipeline import run_summarization

st.set_page_config(page_title="AI Summarizer", layout="centered")

st.title("AI Text Summarizer")
st.markdown("Easily generate summaries from long text or files.")

st.subheader("1. Input Data")
choice = st.radio("How do you want to provide text?", ["Paste Text", "Upload File"], horizontal=True)

text_input = ""

if choice == "Paste Text":
    text_input = st.text_area("Paste your content here:", height=300)

elif choice == "Upload File":
    uploaded_file = st.file_uploader("Choose a .txt file", type="txt")
    if uploaded_file is not None:
        text_input = uploaded_file.read().decode("utf-8")
        st.success("File uploaded successfully!")

st.markdown("---")
st.subheader("2. Results")

if st.button("Generate Summary"):
    if not text_input:
        st.warning("Please provide some text first.")
    else:
        with st.spinner("Summarizing... this might take a moment."):
            try:
                final_result, steps = run_summarization(text_input)
                
                st.success("Done!")
                st.write("### Final Summary")
                st.write(final_result)
                
                with st.expander("See Intermediate Steps"):
                    for i, step in enumerate(steps):
                        st.write(f"Part {i+1}: {step}")
                        
            except Exception as e:
                st.error(f"Something went wrong: {e}")