import re

def limpar_texto(texto: str) -> str:
    texto = re.sub(r"http\S+", "", texto)       # remove links
    texto = re.sub(r"@\w+", "", texto)          # remove menções
    texto = re.sub(r"[^a-zA-ZÀ-ÿ\s]", "", texto) # remove símbolos
    return texto.strip().lower()
