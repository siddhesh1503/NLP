import nltk
from nltk.stem import WordNetLemmatizer

# Download required resources
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

def get_suffix(stem, plural):
    """Get the actual changed part (suffix) from plural"""
    # Start comparing from the left
    i = 0
    while i < min(len(stem), len(plural)) and stem[i] == plural[i]:
        i += 1
    return plural[i:]  # return changed/added part

def fst_noun_parser(word):
    word = word.lower()
    lemmatizer = WordNetLemmatizer()
    
    # Step 1: Get the singular stem
    stem = lemmatizer.lemmatize(word, pos='n')
    is_plural = (stem != word)

    if is_plural:
        suffix = get_suffix(stem, word).upper()
        intermediate_output = f"{stem.upper()} ^ {suffix} #"
        number = "+PL"
    else:
        intermediate_output = f"{stem.upper()} ^ #"
        number = "+SG"

    final_output = ' '.join(stem.upper()) + " +N " + number

    # Show outputs
    print("\nIntermediate Output:", intermediate_output)
    print("Final Output:", final_output)

# === User Input ===
user_input = input("Enter a noun (singular or plural): ")
fst_noun_parser(user_input)