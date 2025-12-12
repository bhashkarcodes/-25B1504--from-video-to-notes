# read the file
with open(r"C:\Users\BHASHKAR\OneDrive\Desktop\WiDS IITB\subtitleByLine.txt", "r") as f:

    text = f.read()

# convert to lowercase
lower_text = text.lower()

# write to new file
with open("LowercasedSubtitle.txt", "w") as f:
    f.write(lower_text)
