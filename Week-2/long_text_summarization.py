from transformers import BartTokenizer, BartForConditionalGeneration
import torch

MODEL_NAME = "facebook/bart-large-cnn"
tokenizer = BartTokenizer.from_pretrained(MODEL_NAME)
model = BartForConditionalGeneration.from_pretrained(MODEL_NAME)


def chunk_text(text, chunk_size=1200, overlap=200):
    """
    Splits long text into overlapping chunks.
    Recommended:
    chunk_size: 800–1400 characters
    overlap: 100–200 characters
    """
    chunks = []
    start = 0
    text_length = len(text)

    while start < text_length:
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start = end - overlap

    return chunks


def summarize_chunk(chunk):
    """
    Summarizes a single text chunk using BART.
    """
    inputs = tokenizer(
        chunk,
        max_length=1024,
        truncation=True,
        return_tensors="pt"
    )

    summary_ids = model.generate(
        inputs["input_ids"],
        max_length=150,
        min_length=60,
        num_beams=4,
        length_penalty=2.0,
        early_stopping=True
    )

    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary



def final_summarize(chunks):
    """
    1. Summarize each chunk
    2. Merge intermediate summaries
    3. Generate final coherent summary
    """
    intermediate_summaries = []

    for i, chunk in enumerate(chunks):
        print(f"Summarizing chunk {i + 1}/{len(chunks)}...")
        summary = summarize_chunk(chunk)
        intermediate_summaries.append(summary)

    merged_text = " ".join(intermediate_summaries)

   
    inputs = tokenizer(
        merged_text,
        max_length=1024,
        truncation=True,
        return_tensors="pt"
    )

    final_ids = model.generate(
        inputs["input_ids"],
        max_length=200,
        min_length=100,
        num_beams=4,
        length_penalty=2.0,
        early_stopping=True
    )

    final_summary = tokenizer.decode(final_ids[0], skip_special_tokens=True)
    return final_summary, intermediate_summaries


if __name__ == "__main__":
   
    with open("transcript.txt", "r", encoding="utf-8") as file:
        text = file.read()

    print("Chunking text...")
    chunks = chunk_text(text)

    print("Running hierarchical summarization...")
    final_summary, chunk_summaries = final_summarize(chunks)


    with open("final_summary.txt", "w", encoding="utf-8") as file:
        file.write(final_summary)

    print(" Final summary saved to final_summary.txt")
