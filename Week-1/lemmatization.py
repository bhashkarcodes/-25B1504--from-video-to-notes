import nltk
nltk.download('wordnet')
nltk.download('omw-1.4')




from nltk.stem import WordNetLemmatizer
from nltk.tokenize import wordpunct_tokenize

lemmatizer = WordNetLemmatizer()

# Read input file
with open(r"C:\Users\BHASHKAR\OneDrive\Desktop\WiDS IITB\StopwordsRemoved.txt",
          "r", encoding="utf-8") as f:
    text = f.read()

# Tokenize
tokens = wordpunct_tokenize(text)

# Lemmatize (only alphabetic words)
lemmatized_tokens = [
    lemmatizer.lemmatize(token.lower())
    for token in tokens
    if token.isalpha()
]

# Write output file
with open(r"C:\Users\BHASHKAR\OneDrive\Desktop\WiDS IITB\LemmatizedText.txt",
          "w", encoding="utf-8") as f:
    f.write(" ".join(lemmatized_tokens))

print("Lemmatization completed and saved to file!")
