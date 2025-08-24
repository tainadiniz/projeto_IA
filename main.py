import pandas as pd
import matplotlib.pyplot as plt
from coletas.coletar_google import coletar_google_news
from processamento.filtro_regex import limpar_texto
from processamento.analise_nlp import analisar_textos
from processamento.analise_nltk import analisar_nltk
from processamento.analise_sentimentos import analisar_sentimentos   # ✅ novo

def main():
    termo = "Inteligência Artificial"
    print(f"📥 Coletando notícias do Google News sobre: {termo}...")
    df_news = coletar_google_news(termo)

    
    if df_news.empty or "texto" not in df_news.columns:
        print("⚠️ Nenhuma notícia encontrada. Encerrando execução.")
        return

    print("🧹 Limpando textos...")
    df_news["texto_limpo"] = df_news["texto"].fillna("").apply(limpar_texto)
    df_news.to_csv("saidas/relatorio.csv", index=False, encoding="utf-8-sig")
    print("💾 Relatório salvo em saidas/relatorio.csv")

   
    print("📊 Analisando textos com spaCy...")
    substantivos, verbos = analisar_textos(df_news["texto_limpo"].tolist())
    substantivos.to_csv("saidas/substantivos.csv", index=False, encoding="utf-8-sig")
    verbos.to_csv("saidas/verbos.csv", index=False, encoding="utf-8-sig")
    print("💾 Resultados spaCy salvos em saidas/substantivos.csv e saidas/verbos.csv")

    print("🔎 Analisando textos com NLTK...")
    df_nltk = analisar_nltk(df_news["texto_limpo"].tolist())
    df_nltk.to_csv("saidas/analise_nltk.csv", index=False, encoding="utf-8-sig")
    print("💾 Resultados NLTK salvos em saidas/analise_nltk.csv")

    print("📝 Analisando sentimentos...")
    df_sent = analisar_sentimentos(df_news["texto_limpo"].tolist())
    df_sent.to_csv("saidas/sentimentos.csv", index=False, encoding="utf-8-sig")
    print("💾 Resultados de sentimentos salvos em saidas/sentimentos.csv")

    plt.figure(figsize=(6,4))
    df_sent["composto"].hist(bins=20, color="purple", alpha=0.7)
    plt.title("Distribuição dos Sentimentos")
    plt.xlabel("Polaridade (negativo → positivo)")
    plt.ylabel("Frequência")
    plt.tight_layout()
    plt.savefig("saidas/sentimentos.png")
    plt.close()
    print("💾 Gráfico de sentimentos salvo em saidas/sentimentos.png")

    print("✅ Projeto finalizado! Confira a pasta /saidas")

if __name__ == "__main__":
    main()
