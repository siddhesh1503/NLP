import nltk
import stanza
from nltk.util import ngrams
from nltk.tokenize import word_tokenize
from nltk.probability import ConditionalFreqDist

# Download resources (first run only)
nltk.download("punkt")
stanza.download("en")

# Initialize stanza pipeline
stanza_nlp = stanza.Pipeline("en", processors="tokenize")


def tokenize_text(text, method="nltk"):
    """Tokenize text using chosen method"""
    if method == "nltk":
        tokens = word_tokenize(text.lower())
    elif method == "stanza":
        doc = stanza_nlp(text)
        tokens = [word.text.lower() for sent in doc.sentences for word in sent.words]
    else:
        raise ValueError("Method must be 'nltk' or 'stanza'")
    return tokens


def generate_ngrams(tokens, n):
    """Generate n-grams with padding"""
    return list(
        ngrams(
            tokens,
            n,
            pad_left=True,
            pad_right=True,
            left_pad_symbol="<s>",
            right_pad_symbol="</s>",
        )
    )


def calculate_probabilities(n_grams):
    """Calculate conditional probabilities for n-grams"""
    cond_freq = ConditionalFreqDist()
    for ng in n_grams:
        history, word = ng[:-1], ng[-1]
        cond_freq[history][word] += 1

    cond_prob = {}
    for history in cond_freq:
        total_hist = sum(cond_freq[history].values())
        for word in cond_freq[history]:
            cond_prob[(history, word)] = cond_freq[history][word] / total_hist
    return cond_prob


def display_output(n, cond_prob):
    print(f"\n===== {n}-GRAM MODEL =====")
    for (history, word), prob in cond_prob.items():
        if history == ():  # Unigram
            print(f"P({word}) = {prob:.3f}")
        else:
            print(f"P({word} | {history}) = {prob:.3f}")


def main():
    text = input("Enter a paragraph: ").strip()
    method = input("Choose tokenizer (nltk/stanza): ").strip().lower()

    tokens = tokenize_text(text, method)
    print("\nTokens:", tokens)

    for n in [1, 2, 3]:  # unigram, bigram, trigram
        n_grams = generate_ngrams(tokens, n)
        cond_prob = calculate_probabilities(n_grams)
        display_output(n, cond_prob)


if __name__ == "__main__":
    main()
