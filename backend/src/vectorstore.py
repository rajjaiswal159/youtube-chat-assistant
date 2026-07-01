# Import Google embedding model
from langchain_google_genai import GoogleGenerativeAIEmbeddings

# Import FAISS vector store
from langchain_community.vectorstores import FAISS

# Load environment variables
from dotenv import load_dotenv

import os

# Load .env variables
load_dotenv()


# Create a vector store from text chunks
def create_vector_store(chunks):

    try:
        # Initialize the embedding model
        embeddings = GoogleGenerativeAIEmbeddings(
            model="gemini-embedding-001"
        )
    
        # Create the FAISS vector store
        vector_store = FAISS.from_texts(
            texts=chunks,
            embedding=embeddings
        )
    
        # Return the vector store
        return vector_store

    # Handle vector store creation errors
    except Exception as e:
        raise RuntimeError(
            f"Failed to create vector store: {e}"
        ) from e
    

# Save the vector store to disk
def save_vector_store(vector_store, video_id):
    path = os.path.join("vector_store", video_id)
    vector_store.save_local(path)


# Load a saved vector store
def load_vector_store(video_id):

    path = os.path.join("vector_store", video_id)

    # Return None if the vector store doesn't exist
    if not os.path.exists(path):
        return None

    # Initialize the embedding model
    embeddings = GoogleGenerativeAIEmbeddings(
        model="gemini-embedding-001"
    )

    # Load and return the vector store
    return FAISS.load_local(
        path,
        embeddings,
        allow_dangerous_deserialization=True
    )
