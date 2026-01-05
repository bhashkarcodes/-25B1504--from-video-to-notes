from nltk.tokenize import wordpunct_tokenize

# Read input file
with open(r"C:\Users\BHASHKAR\OneDrive\Desktop\WiDS IITB\StopwordsRemoved.txt",
          "r", encoding="utf-8") as f:
    text = f.read()

# Tokenize text
tokens = wordpunct_tokenize(text)

# Write tokens to output file
with open(r"C:\Users\BHASHKAR\OneDrive\Desktop\WiDS IITB\TokenizedText.txt",
          "w", encoding="utf-8") as f:
    f.write(" ".join(tokens))

print("Tokenized text saved successfully!")
