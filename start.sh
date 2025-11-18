#!/bin/bash

# 1. Limpeza forçada
echo "🧹 1. Limpando instalações antigas..."
rm -rf venv

# 2. Criação do ambiente
echo "📦 2. Criando ambiente virtual (venv)..."
python3 -m venv venv

# 3. Instalação explícita
echo "⬇️  3. Instalando bibliotecas (Aguarde...)"
# O segredo: instalar o langchain SOZINHO primeiro para garantir
./venv/bin/pip install --upgrade pip
./venv/bin/pip install langchain
./venv/bin/pip install langchain-community langchain-groq langchain-huggingface chromadb pypdf python-dotenv

# 4. Prova real
echo "🔍 4. Verificando o que foi instalado:"
./venv/bin/pip list | grep langchain

# 5. Execução
echo "🚀 5. Iniciando o Agente..."
./venv/bin/python app.py