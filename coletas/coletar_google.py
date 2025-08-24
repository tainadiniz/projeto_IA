import requests
from bs4 import BeautifulSoup
import pandas as pd

def coletar_google_news(termo="Inteligência Artificial"):
    url = f"https://news.google.com/rss/search?q={termo}&hl=pt-BR&gl=BR&ceid=BR:pt-419"
    resposta = requests.get(url, timeout=10)
    sopa = BeautifulSoup(resposta.text, "xml")

    noticias = []
    for item in sopa.find_all("item")[:30]:
        titulo = item.title.text
        link = item.link.text
        noticias.append({"fonte": link, "texto": titulo})

    if noticias:
        return pd.DataFrame(noticias)
    else:
        return pd.DataFrame([{"fonte": url, "texto": "Nenhuma notícia encontrada"}])
