import nltk
from nltk.corpus import stopwords

# Download stopwords (run once)
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

# Read input file
with open(r"C:\Users\BHASHKAR\OneDrive\Desktop\WiDS IITB\Spellingcorrected.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Remove stop words
filtered_words = [
    word for word in text.split()
    if word.lower() not in stop_words
]

# Write output file
with open("StopwordsRemoved.txt", "w", encoding="utf-8") as f:
    f.write(" ".join(filtered_words))

print("Stop words removed successfully!")
