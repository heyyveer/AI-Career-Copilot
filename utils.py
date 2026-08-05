from dotenv import load_dotenv

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_groq import ChatGroq
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

load_dotenv()

# LLM
llm = ChatGroq(
    model_name="llama-3.3-70b-versatile",
    temperature=0.5,
)

# Embedding Model

embedding_model = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5"
)


def load_vector_store(index_path: str = "vector_store"):
    """
    Load saved FAISS vector database.
    """

    return FAISS.load_local(
        folder_path=index_path,
        embeddings=embedding_model,
        allow_dangerous_deserialization=True,
    )


def generate(system_prompt: str, human_prompt: str):
    """
    Generate response using LLM.
    """

    response = llm.invoke(
        [
            SystemMessage(content=system_prompt),
            HumanMessage(content=human_prompt),
        ]
    )

    return response.content