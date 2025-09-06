irregulars = {
    "children": "child",
    "men": "man",
    "women": "woman",
    "mice": "mouse",
    "geese": "goose",
    "oxen": "ox",
    "teeth": "tooth",
    "feet": "foot",
    "people": "person",
    "lice": "louse",
    "cacti": "cactus",
    "fungi": "fungus",
    "nuclei": "nucleus",
    "alumni": "alumnus",
    "syllabi": "syllabus",
    "crises": "crisis",
    "theses": "thesis",
    "analyses": "analysis"
}

word = input("Enter a noun: ").lower()

state = "q0"
root = ""
feature = "" 
suffix = ""

if state == "q0":
    if word in irregulars:
        root = irregulars[word]
        feature = "PLURAL"
        suffix = word[len(root):]
        state = "qf"

    elif len(word) > 3 and word.endswith("ies"):
        root = word[:-3] + "y"
        feature = "PLURAL"
        suffix = "IES"
        state = "qf"

    elif len(word) > 3 and word.endswith("ves"):
        root = word[:-3] + "fe"
        feature = "PLURAL"
        suffix = "VES"
        state = "qf"

    elif len(word) > 2 and word.endswith("es"):
        root = word[:-2]
        feature = "PLURAL"
        suffix = "ES"
        state = "qf"

    elif len(word) > 2 and word.endswith("en"):   # NEW generic -en plural rule
        root = word[:-2]
        feature = "PLURAL"
        suffix = "EN"
        state = "qf"

    elif len(word) > 1 and word.endswith("s"):
        root = word[:-1]
        feature = "PLURAL"
        suffix = "S"
        state = "qf"

    else:
        root = word
        feature = "SINGULAR"
        suffix = ""
        state = "qf"


print("\nIntermediate Output:", root.upper(), "^", suffix, "#")
print("Final Output:", ' '.join(root.upper()), "+N +" + ("PL" if feature == "PLURAL" else "SG"))
