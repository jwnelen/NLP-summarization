from datasets import load_dataset
from transformers import pipeline

raw_dataset = load_dataset('cnn_dailymail', '3.0.0')

classifier = pipeline("summarization")

if __name__ == '__main__':
    pass
