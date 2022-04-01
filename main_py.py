from datasets import load_dataset
from transformers import pipeline

raw_dataset = load_dataset('cnn_dailymail', '3.0.0')

classifier = pipeline("summarization")

if __name__ == '__main__':
    for i in range(10):
        article = raw_dataset["train"][i]
        summary = classifier(article)
        print(summary)
