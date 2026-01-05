from transformers import pipeline

classifier = pipeline("sentiment-analysis")

res = classifier("I am very sad today")

print(res)