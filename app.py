import os
import sys
from dotenv import load_dotenv

# Carrega as chaves
load_dotenv()

# --- IMPORTAÇÕES SEGURAS ---
# (Removemos 'langchain.chains' que estava dando erro)
try:
    from langchain_community.document_loaders import PyPDFLoader
    from langchain_text_splitters import RecursiveCharacterTextSplitter
    from langchain_community.vectorstores import Chroma
    from langchain_huggingface import HuggingFaceEmbeddings
    from langchain_groq import ChatGroq
except ImportError as e:
    print(f"Erro de Instalação: {e}")
    sys.exit(1)

# Configurações
ARQUIVO_MANUAL = "manual.pdf"

def main():
    print("\n🤖 --- AGENTE RAG (MODO MANUAL) ---")
    
    # 1. Validação
    if not os.getenv("GROQ_API_KEY"):
        print("❌ ERRO: Chave GROQ_API_KEY não configurada no .env")
        return
    
    if not os.path.exists(ARQUIVO_MANUAL):
        print(f"❌ ERRO: Arquivo '{ARQUIVO_MANUAL}' não encontrado.")
        return

    # 2. Carregar PDF
    print("1. Lendo PDF...")
    loader = PyPDFLoader(ARQUIVO_MANUAL)
    docs = loader.load()

    # 3. Dividir Texto
    print("2. Processando texto...")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splits = text_splitter.split_documents(docs)

    # 4. Criar Banco de Dados (Embeddings)
    print("3. Indexando memória (pode demorar 1 min)...")
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    
    vectorstore = Chroma.from_documents(
        documents=splits,
        embedding=embeddings,
        persist_directory="./chroma_db" # Salva no disco
    )

    # 5. Configurar LLM (Groq)
    print("4. Conectando ao Llama 3...")
    llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0)

    print("\n✅ SISTEMA PRONTO! Pergunte algo.")
    print("-----------------------------------")

    while True:
        pergunta = input("\nVocê: ")
        if pergunta.lower() in ["sair", "fim", "exit"]:
            break
        
        print("🔍 Pesquisando no manual...")
        
        # --- A MÁGICA DO RAG MANUAL (Aqui substituímos o RetrievalQA) ---
        
        # Passo A: Recuperação (Retrieval)
        # Buscamos os 3 trechos mais parecidos com a pergunta
        docs_retornados = vectorstore.similarity_search(pergunta, k=3)
        
        # Juntamos o texto desses trechos para formar o contexto
        contexto = "\n\n".join([doc.page_content for doc in docs_retornados])
        
        # Passo B: Montagem do Prompt
        prompt_final = (
            f"Você é um assistente técnico útil. Use APENAS o contexto abaixo para responder à pergunta do usuário.\n"
            f"Se a resposta não estiver no contexto, diga que não sabe.\n\n"
            f"--- CONTEXTO DO MANUAL ---\n{contexto}\n"
            f"--------------------------\n\n"
            f"PERGUNTA DO USUÁRIO: {pergunta}"
        )
        
        # Passo C: Geração (Generation)
        try:
            resposta = llm.invoke(prompt_final)
            print(f"\n🤖 Agente: {resposta.content}")
            
            # Mostra a fonte (Critério da atividade)
            fonte = docs_retornados[0].metadata.get('page', '?')
            print(f"[Info retirada da página {fonte}]")
            
        except Exception as e:
            print(f"Erro ao gerar resposta: {e}")

if __name__ == "__main__":
    main()