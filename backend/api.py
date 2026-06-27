from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.transcript import get_transcript
from src.text_splitter import split_text
from src.vectorstore import create_vector_store
from src.chatbot import create_rag_chain

app = FastAPI(
    title="YouTube Chat API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global variables
vector_store = None
rag_chain = None


@app.get("/")
def home():
    return {"status": "Backend Running"}


@app.post("/process")
async def process_video(data: dict):

    global vector_store
    global rag_chain

    try:

        video_url = data["video_url"]

        transcript = get_transcript(video_url)

        chunks = split_text(transcript)

        vector_store = create_vector_store(chunks)

        rag_chain = create_rag_chain(vector_store)

        return {
            "success": True,
            "message": "Video processed successfully!"
        }

    except Exception as e:

        return {
            "success": False,
            "message": str(e)
        }


@app.post("/chat")
async def chat(data: dict):

    global rag_chain

    try:

        if rag_chain is None:
            return {
                "success": False,
                "message": "Please process a video first."
            }

        question = data["question"]

        answer = rag_chain.invoke(question)

        return {
            "success": True,
            "answer": answer
        }

    except Exception as e:

        return {
            "success": False,
            "message": str(e)
        }