# Import Google embedding model
from langchain_google_genai import GoogleGenerativeAIEmbeddings

# Import FAISS
from langchain_community.vectorstores import FAISS

# Load environment variables
from dotenv import load_dotenv

# Load .env variables
load_dotenv()


# Create and save vector store
def create_vector_store(chunks):

    # Initialize embedding model
    embeddings = GoogleGenerativeAIEmbeddings(
        model="gemini-embedding-001"
    )

    # Create FAISS index
    vector_store = FAISS.from_texts(
        texts=chunks,
        embedding=embeddings
    )

    # Return vector store
    return vector_store
