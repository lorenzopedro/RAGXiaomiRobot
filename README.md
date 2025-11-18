# Agente RAG - Manual do Robô Aspirador 🤖🧹

Este projeto consiste em um **Agente de Inteligência Artificial com RAG (Retrieval-Augmented Generation)** capaz de responder perguntas técnicas baseadas em um manual de instruções (PDF) de um robô aspirador.

O projeto foi desenvolvido como atividade avaliativa da disciplina de Machine Learning/IA.

## 📋 Funcionalidades
- **Ingestão de Dados:** Lê e processa documentos PDF.
- **Busca Semântica:** Utiliza banco vetorial (ChromaDB) para encontrar trechos relevantes do manual.
- **Geração de Respostas:** Integração com LLM (Llama 3 via Groq) para formular respostas naturais.
- **Citação de Fontes:** Indica a página do manual de onde a informação foi retirada.

## 🛠️ Tecnologias Utilizadas
- **Linguagem:** Python
- **Framework:** LangChain (Community & Core)
- **LLM:** Llama 3 (via Groq API - Gratuito e Rápido)
- **Embeddings:** HuggingFace (all-MiniLM-L6-v2 - Execução Local)
- **Vector Store:** ChromaDB

## 🚀 Como Executar

### 1. Pré-requisitos
- Python 3.10+
- Uma chave de API gratuita da [Groq](https://console.groq.com/)

### 2. Instalação
Clone o repositório e instale as dependências:

```bash
pip install langchain langchain-community langchain-groq langchain-huggingface chromadb pypdf python-dotenv