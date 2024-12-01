from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter

def load_and_parse_pdf(file_path):
    """Load and parse PDF using PyPDFLoader."""
    try:
        loader = PyPDFLoader(file_path)
        documents = loader.load()
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=50)
        return text_splitter.split_documents(documents)
    except Exception as e:
        print(f"Error loading PDF: {str(e)}")
        return None
