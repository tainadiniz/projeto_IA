from nltk.sentiment import SentimentIntensityAnalyzer
import pandas as pd
import nltk
nltk.download("vader_lexicon")

# Inicializa o analisador
sia = SentimentIntensityAnalyzer()

def analisar_sentimentos(textos):
    resultados = []

    for txt in textos:
        scores = sia.polarity_scores(txt)
        resultados.append({
            "texto": txt,
            "positivo": scores["pos"],
            "negativo": scores["neg"],
            "neutro": scores["neu"],
            "composto": scores["compound"]
        })

    return pd.DataFrame(resultados)
