from langchain.embeddings.huggingface import HuggingFaceEmbeddings

def tokenize_and_embed(documents):
    """Convert parsed documents into embeddings."""
    try:
        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
        return [embeddings.embed_query(doc.page_content) for doc in documents]
    except Exception as e:
        print(f"Error during tokenization or embedding: {str(e)}")
        return None
