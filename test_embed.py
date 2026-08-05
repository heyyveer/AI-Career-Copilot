import os
from dotenv import load_dotenv

load_dotenv()

print("KEY:", os.getenv("GOOGLE_API_KEY")[:10])

from langchain_google_genai import GoogleGenerativeAIEmbeddings

emb = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-2"
)

print(emb.embed_query("hello"))