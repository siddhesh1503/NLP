import re
import nltk
from collections import defaultdict, Counter

nltk.download('punkt')

# ----------- Preprocessing -----------
def preprocess_text(text):
    # Lowercase + remove punctuation (keep only words)
    text = text.lower()
    tokens = nltk.word_tokenize(text)
    tokens = [re.sub(r'[^a-z]', '', token) for token in tokens]
    tokens = [token for token in tokens if token != '']  # remove empty tokens
    return tokens

# ----------- N-gram Model with Laplace Smoothing -----------
def build_ngram(tokens, n):
    ngrams = []
    for i in range(len(tokens)-n+1):
        ngrams.append(tuple(tokens[i:i+n]))
    return ngrams

def laplace_smoothing(ngrams, n, context):
    context_counts = Counter()
    word_counts = defaultdict(int)
    vocab = set()

    for gram in ngrams:
        prefix = gram[:-1]
        word = gram[-1]
        vocab.add(word)
        if prefix == context:
            word_counts[word] += 1
        if len(prefix) == len(context) and prefix == context:
            context_counts[prefix] += 1

    V = len(vocab)
    total_context = sum(word_counts.values())

    probs = {}
    for word in vocab:
        count_word = word_counts[word]
        # Laplace smoothing
        probs[word] = (count_word + 1) / (total_context + V)

    return probs

# ----------- Next Word Prediction -----------
def predict_next_word(text, n, context):
    tokens = preprocess_text(text)
    ngrams = build_ngram(tokens, n)

    # Convert context to tuple
    context = tuple(preprocess_text(context))

    probs = laplace_smoothing(ngrams, n, context)

    if not probs:
        return None, {}

    predicted = max(probs, key=probs.get)
    return predicted, probs

# ----------- Main Program -----------
if __name__ == "__main__":
    print("=== Next Word Prediction using Laplace Smoothing ===\n")
    text = input("Enter your paragraph:\n")
    n = int(input("Choose N for N-gram (2 for bigram, 3 for trigram): "))
    context = input(f"Enter the context ({n-1} words): ")

    predicted, probs = predict_next_word(text, n, context)

    print("\n--- Probabilities (Laplace Smoothing) ---")
    for word, p in probs.items():
        print(f"P({word} | {context}) = {p:.4f}")

    if predicted:
        print(f"\n Predicted Next Word: {predicted}")
    else:
        print("\n No prediction available (context unseen).")
