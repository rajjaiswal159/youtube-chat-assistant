from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.transcript import get_transcript
from src.text_splitter import split_text
from src.vectorstore import create_vector_store

app = FastAPI(
    title="YouTube Chat API",
    version="1.0.0"
)

# Allow Chrome Extension
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # Development only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Store vector store in memory
vector_store = None


@app.get("/")
def home():
    return {
        "status": "Backend Running"
    }


@app.post("/process")
async def process_video(data: dict):

    global vector_store

    try:

        video_url = data["video_url"]

        transcript = get_transcript(video_url)

        chunks = split_text(transcript)

        vector_store = create_vector_store(chunks)

        return {
            "success": True,
            "message": "Video processed successfully!"
        }

    except Exception as e:

        return {
            "success": False,
            "message": str(e)
        }