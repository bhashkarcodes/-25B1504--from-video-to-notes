from transformers import BartTokenizer, BartForConditionalGeneration
import streamlit as st

@st.cache_resource
def load_model():
    print("Loading BART Model...")
    model_name = "facebook/bart-large-cnn"
    tokenizer = BartTokenizer.from_pretrained(model_name)
    model = BartForConditionalGeneration.from_pretrained(model_name)
    print("BART Model Loaded.")
    return tokenizer, model

tokenizer, model = load_model()