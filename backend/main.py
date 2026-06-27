from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="YouTube Chat API",
    version="1.0.0"
)

# Enable CORS (Development only)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "message": "Backend is running!"
    }

@app.post("/test")
async def test(data: dict):

    print(data)

    return {
        "message": "Backend connected successfully!"
    }