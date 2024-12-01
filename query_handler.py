from langchain.vectorstores import FAISS
from langchain.embeddings.huggingface import HuggingFaceEmbeddings

def query_pdf(documents, query):
    """Handle user queries using FAISS."""
    try:
        vector_store = FAISS.from_documents(documents, HuggingFaceEmbeddings())
        results = vector_store.similarity_search(query)
        return results
    except Exception as e:
        print(f"Error during querying: {str(e)}")
        return None
