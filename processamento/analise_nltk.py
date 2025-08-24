import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import RSLPStemmer, WordNetLemmatizer
import pandas as pd
import re

recursos = {
    "punkt": "tokenizers/punkt",
    "punkt_tab": "tokenizers/punkt_tab/portuguese",
    "rslp": "stemmers/rslp",
    "wordnet": "corpora/wordnet"
}
for recurso, path in recursos.items():
    try:
        nltk.data.find(path)
    except LookupError:
        nltk.download(recurso, quiet=True)

def analisar_nltk(textos):
    stemmer = RSLPStemmer()
    lemmatizer = WordNetLemmatizer()

    resultados = []

    for txt in textos:
    
        tokens = word_tokenize(txt, language="portuguese")

        tokens = [t.lower() for t in tokens if re.match(r"[a-zA-ZÀ-ÿ]", t)]

        # Stemming e Lematização
        stems = [stemmer.stem(t) for t in tokens]
        lemas = [lemmatizer.lemmatize(t) for t in tokens]

        resultados.append({
            "texto": txt,
            "tokens": " ".join(tokens),
            "stems": " ".join(stems),
            "lemas": " ".join(lemas)
        })

    return pd.DataFrame(resultados)
