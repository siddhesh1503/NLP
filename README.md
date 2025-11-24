# NLP

> A collection of natural language processing experiments, practical notebooks and scripts by Siddhesh Shinde.

## About

This repository contains several Jupyter notebooks and Python scripts exploring classical and modern NLP tasks — experiments, practical exercises, and small projects. The work includes information retrieval using Hugging Face + Pinecone, word sense disambiguation (WSD), storytelling bot experiments, and multiple hands-on notebooks for learning core NLP techniques.

---

## Repository structure

* `Document_Retrieval_HuggingFace_Pinecone.ipynb`
  Retrieval/semantic search experiment using Hugging Face embeddings and Pinecone vector DB.

* `Document_Retrieval_HuggingFace_Pinecone.ipynb` (duplicate link shown in repo listing)

* `NLP_EXP_7.ipynb`, `NLP_EXP_8.ipynb`, `NLP_EXP_9.ipynb`
  Series of experiment notebooks (tokenization, embeddings, classification, etc.).

* `NLP_Experiment_5_Siddhesh_Shinde.ipynb`, `NLP_Practical_2_Siddhesh.ipynb`, `NLP_Project.ipynb`
  Practical exercises and a capstone-style notebook for an NLP project.

* `Story_Telling_Bot.ipynb`
  Notebook experimenting with sequence generation / story generation models.

* `WSD.ipynb`
  Word Sense Disambiguation experiments.

* Python scripts: `EXP3.py`, `exp4.py`, `exp6.py`, `expi4.py`, `expi6.py`, `expriment6.py`
  Small runnable experiments and utility scripts.

* `README.md`
  This file.

> Note: Most of the repository content is written as Jupyter notebooks (majority of files). See the file list for details.

---

## Requirements

These notebooks were developed with a typical Python data-science environment. Suggested setup:

1. Install Python 3.9+ (3.8 also usually works).
2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # macOS / Linux
venv\Scripts\activate     # Windows
```

3. Install dependencies. If there's no `requirements.txt` in the repo, install packages below:

```bash
pip install jupyterlab notebook numpy pandas scikit-learn matplotlib nltk spacy transformers sentence-transformers pinecone-client datasets tqdm
```

4. Additional model/data setup (if used in notebooks):

   * For `spacy` models: `python -m spacy download en_core_web_sm`
   * For NLTK: run a quick downloader inside Python/Jupyter:

```py
import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
```

5. Pinecone (if using `Document_Retrieval_HuggingFace_Pinecone.ipynb`): create a Pinecone account and set `PINECONE_API_KEY` and `PINECONE_ENV` as environment variables before running that notebook.

6. Hugging Face Transformer models used in notebooks may require additional downloads; ensure you have internet access when running those cells.

---

## How to run

1. Clone the repo:

```bash
git clone https://github.com/siddhesh1503/NLP.git
cd NLP
```

2. Start Jupyter Lab / Notebook:

```bash
jupyter lab
# or
jupyter notebook
```

3. Open any `.ipynb` file and run cells in order. For script files (`.py`), run them using:

```bash
python EXP3.py
```

---

## Short descriptions & tips

* The notebooks are exploratory and may contain experimental cells. If a cell fails due to missing API keys or models, read the top cells of that notebook — they often indicate required keys or model names.
* If you want to reproduce a notebook exactly, check for hidden configuration cells that set paths, API keys or dataset locations.
* If you'd like, I can help:

  * create a `requirements.txt` from the notebooks,
  * add clear README badges and a short overview for each notebook,
  * or convert key notebooks into reproducible `.py` scripts or a small demo app.

---

## Contribution

Contributions are welcome. If you want to improve this repository:

1. Fork the project.
2. Create a feature branch: `git checkout -b feature/my-change`.
3. Commit your changes and open a pull request.

---

## License

No license specified. If you want this to be open-source, consider adding a `LICENSE` file (e.g., MIT, Apache-2.0).

---

## Contact

For questions or help adapting notebooks into projects, reach out via the GitHub profile: `https://github.com/siddhesh1503`.
