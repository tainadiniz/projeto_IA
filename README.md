# Projeto IA no Dia a Dia

Este projeto coleta e analisa textos relacionados à **Inteligência Artificial no dia a dia**, com foco em como ferramentas como ChatGPT, Gemini e Copilot estão sendo discutidas em sites de notícias.

## 🎯 Objetivos
- Coletar manchetes de sites de notícias brasileiros.
- Limpar textos com regex.
- Analisar textos com NLP (spaCy).
- Gerar relatórios e visualizações (nuvem de palavras, substantivos e verbos mais frequentes).

## 🚀 Como Rodar
1. Crie o ambiente virtual:
   ```bash
   python -m venv .venv
   Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
   source .venv/bin/activate   # Linux/Mac
   .venv\Scripts\activate    # Windows
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Baixe o modelo do spaCy:
   ```bash
   python -m spacy download pt_core_news_sm
   ```
4. Execute o projeto:
   ```bash
   python main.py
   ```

## 📦 Dependências
- requests
- beautifulsoup4
- pandas
- matplotlib
- wordcloud
- spacy
