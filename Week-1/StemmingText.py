from nltk.stem import PorterStemmer
from nltk.tokenize import wordpunct_tokenize

stemmer = PorterStemmer()

# Read input file
with open(r"C:\Users\BHASHKAR\OneDrive\Desktop\WiDS IITB\TokenizedText.txt",
          "r", encoding="utf-8") as f:
    text = f.read()

# Tokenize
tokens = wordpunct_tokenize(text)

# Stem tokens (only alphabetic words)
stemmed_tokens = [
    stemmer.stem(token) for token in tokens if token.isalpha()
]

# Write to output file
with open(r"C:\Users\BHASHKAR\OneDrive\Desktop\WiDS IITB\StemmedText.txt",
          "w", encoding="utf-8") as f:
    f.write(" ".join(stemmed_tokens))

print("Stemming completed and saved to file!")
