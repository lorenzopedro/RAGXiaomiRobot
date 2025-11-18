# Agente RAG - Manual do Robô Aspirador 🤖🧹

Este projeto é um **Agente de Inteligência Artificial** que utiliza a técnica **RAG (Retrieval-Augmented Generation)** para responder dúvidas técnicas baseadas no PDF de um manual de robô aspirador.

O sistema lê o manual, encontra as partes relevantes e usa o modelo **Llama 3** para formular uma resposta precisa, citando a página da fonte.

## 📋 Funcionalidades
- **Busca Inteligente:** Encontra informações no PDF mesmo que a pergunta use termos diferentes.
- **Sem Custo:** Utiliza APIs e modelos gratuitos (Groq + HuggingFace).
- **Citação de Fontes:** Indica em qual página do manual a informação foi encontrada.
- **Memória Persistente:** Salva o banco de dados vetorial localmente para não precisar reler o PDF toda vez.

## 🛠️ Tecnologias
- **Linguagem:** Python 3.10+
- **LLM:** Llama 3 (via Groq API)
- **Embeddings:** HuggingFace (`all-MiniLM-L6-v2`)
- **Vector Store:** ChromaDB
- **Framework:** LangChain

---

## 🚀 Como Rodar o Projeto

Siga os passos abaixo para executar o agente no seu computador ou Codespaces.

### 1. Configuração Inicial
Primeiro, clone este repositório. Em seguida, crie um arquivo chamado `.env` na raiz do projeto e adicione sua chave da Groq (gratuita em [console.groq.com](https://console.groq.com)):

```env
GROQ_API_KEY=gsk_sua_chave_aqui...
2. Instalação das Dependências
É recomendado usar um ambiente virtual para não conflitar com outras instalações.

Bash

# 1. Criar o ambiente virtual
python3 -m venv venv

# 2. Instalar as bibliotecas necessárias
./venv/bin/pip install -r requirements.txt
(Caso não tenha o arquivo requirements.txt, instale manualmente com: ./venv/bin/pip install langchain langchain-community langchain-groq langchain-huggingface chromadb pypdf python-dotenv)

3. Executando o Agente
Certifique-se de que o arquivo manual.pdf está na pasta principal.

Opção A (Recomendada - Direta): Rode este comando para usar o Python do ambiente virtual diretamente:

Bash

./venv/bin/python app.py
Opção B (Tradicional): Ative o ambiente e depois rode:

Bash

source venv/bin/activate
python app.py
🧠 Como funciona (RAG Manual)
Para fins didáticos e de performance, este projeto implementa a lógica RAG manualmente:

Loader: Carrega o PDF.

Splitter: Divide o texto em pedaços de 1000 caracteres.

Retrieval: O vectorstore.similarity_search busca os 3 trechos mais parecidos com a pergunta.

Generation: Um prompt é montado combinando esses trechos + a pergunta do usuário e enviado ao Llama 3.

📁 Estrutura de Arquivos Importantes
app.py: Código principal do agente.

manual.pdf: Base de conhecimento (substitua pelo manual que desejar).

requirements.txt: Lista de bibliotecas necessárias.

.env: Arquivo de configuração de senhas (Não versionado no Git).

Autor: Lorenzo Pedro Freitas Silva