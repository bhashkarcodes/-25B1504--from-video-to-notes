from summarizer.model import tokenizer, model
from summarizer.chunking import chunk_text
from utils.helpers import clean_text

def summarize_one_chunk(chunk):
    inputs = tokenizer(chunk, max_length=1024, truncation=True, return_tensors="pt")
    
    summary_ids = model.generate(
        inputs["input_ids"], 
        max_length=150, 
        min_length=50, 
        length_penalty=2.0, 
        num_beams=4, 
        early_stopping=True
    )
    
    return tokenizer.decode(summary_ids[0], skip_special_tokens=True)

def run_summarization(text):
    clean_data = clean_text(text)
    chunks = chunk_text(clean_data)
    
    partial_summaries = []
    for chunk in chunks:
        summary = summarize_one_chunk(chunk)
        partial_summaries.append(summary)
        
    combined_text = " ".join(partial_summaries)
    
    final_inputs = tokenizer(combined_text, max_length=1024, truncation=True, return_tensors="pt")
    final_ids = model.generate(
        final_inputs["input_ids"], 
        max_length=250, 
        min_length=60, 
        length_penalty=2.0, 
        num_beams=4, 
        early_stopping=True
    )
    
    final_summary = tokenizer.decode(final_ids[0], skip_special_tokens=True)
    return final_summary, partial_summaries