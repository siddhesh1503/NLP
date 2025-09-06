import nltk
from collections import defaultdict, Counter
import stanza

# Download resources once
nltk.download("punkt", quiet=True)
stanza.download("en")   # <-- FIXED (removed quiet=True)
nlp = stanza.Pipeline("en", processors="tokenize", use_gpu=False, verbose=False)

# --- Tokenizers ---
def tokenize_text(text, method="nltk"):
    if method == "nltk":
        return nltk.word_tokenize(text.lower())
    elif method == "stanza":
        doc = nlp(text)
        return [word.text.lower() for sent in doc.sentences for word in sent.words]
    else:
        raise ValueError("Choose tokenizer: nltk or stanza")

# --- Build N-grams ---
def build_ngram(tokens, n):
    ngrams = defaultdict(Counter)
    for i in range(len(tokens) - n + 1):
        context = tuple(tokens[i : i + n - 1])
        next_word = tokens[i + n - 1]
        ngrams[context][next_word] += 1
    return ngrams

# --- Laplace Smoothing ---
def laplace_predict(ngrams, context, vocab):
    context_counts = ngrams.get(context, Counter())
    total_context = sum(context_counts.values())
    V = len(vocab)

    print("\n=== Detailed Laplace Smoothing Computation ===")
    print(f"Context: {context}\n")
    print("Step-by-step probabilities:")

    probs = {}
    for word in vocab:
        prob = (context_counts[word] + 1) / (total_context + V)
        probs[word] = prob
        print(f"P({word} | {context}) = ({context_counts[word]} + 1) / ({total_context} + {V}) = {prob:.4f}")

    predicted_word = max(probs, key=probs.get)
    print(f"\n Predicted Next Word: {predicted_word}")

# --- Main ---
def main():
    print("=== Next Word Prediction using Laplace Smoothing ===\n")
    print("Enter your paragraph (type END to finish):")

    lines = []
    while True:
        line = input()
        if line.strip().lower() == "end":
            break
        lines.append(line)
    text = " ".join(lines)

    method = input("Choose tokenizer (nltk/stanza): ").strip().lower()
    n = int(input("Choose N for N-gram (2=bigram, 3=trigram, 4=fourgram): "))

    tokens = tokenize_text(text, method)
    vocab = set(tokens)

    ngrams = build_ngram(tokens, n)

    required_context_len = n - 1
    context_input = input(f"Enter the context (last {required_context_len} words): ").lower().split()

    if len(context_input) != required_context_len:
        print(f"\n Error: {n}-gram requires {required_context_len} words of context, "
              f"but you provided {len(context_input)}.\n")
        return

    context = tuple(context_input)
    laplace_predict(ngrams, context, vocab)

if __name__ == "__main__":
    main()
