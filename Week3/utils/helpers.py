def clean_text(text):
    text = text.replace("\r", " ")
    text = text.replace("\n", " ")
    text = " ".join(text.split())
    return text