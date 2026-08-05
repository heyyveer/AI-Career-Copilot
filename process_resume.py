from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS

load_dotenv()

embedding_model = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5"
)

def process_resume(
    pdf_path: str,
    index_path: str = "vector_store",
):
    """
    Process the uploaded resume and create a FAISS vector database.
    """

    # Load PDF
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    # Split Resume
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
    )

    chunks = splitter.split_documents(documents)

    # Create FAISS Index
    vector_store = FAISS.from_documents(
        documents=chunks,
        embedding=embedding_model,
    )

    # Save Index
    vector_store.save_local(index_path)

    return vector_store