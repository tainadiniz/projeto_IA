import spacy
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

nlp = spacy.load("pt_core_news_sm")

def analisar_textos(textos):
    tokens, lemas, substantivos, verbos = [], [], [], []

    for txt in textos:
        doc = nlp(txt)
        for token in doc:
            if not token.is_stop and not token.is_punct:
                tokens.append(token.text)
                lemas.append(token.lemma_)
                if token.pos_ == "NOUN":
                    substantivos.append(token.lemma_)
                if token.pos_ == "VERB":
                    verbos.append(token.lemma_)

    freq_nouns = Counter(substantivos).most_common(10)
    freq_verbs = Counter(verbos).most_common(10)

    if freq_nouns:
        df_nouns = pd.DataFrame(freq_nouns, columns=["Substantivo", "Frequência"])
        df_nouns.plot(kind="bar", x="Substantivo", y="Frequência", legend=False, color="skyblue")
        plt.title("Top 10 Substantivos")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig("saidas/substantivos.png")
        plt.close()
        

    if freq_verbs:
        df_verbs = pd.DataFrame(freq_verbs, columns=["Verbo", "Frequência"])
        df_verbs.plot(kind="bar", x="Verbo", y="Frequência", legend=False, color="lightgreen")
        plt.title("Top 10 Verbos")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig("saidas/verbos.png")
        plt.close()

    if lemas:
        wc = WordCloud(width=800, height=400, background_color="white").generate(" ".join(lemas))
        plt.imshow(wc, interpolation="bilinear")
        plt.axis("off")
        plt.savefig("saidas/nuvem_palavras.png")
        plt.close()

    return (
        pd.DataFrame(freq_nouns, columns=["Substantivo", "Frequência"]),
        pd.DataFrame(freq_verbs, columns=["Verbo", "Frequência"])
    )
