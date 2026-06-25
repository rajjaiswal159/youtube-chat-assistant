# Import transcript function
from src.transcript import get_transcript

# Import text splitter function
from src.text_splitter import split_text

# YouTube URL
url = "https://www.youtube.com/watch?v=aircAruvnKk"

# Get transcript
transcript = get_transcript(url)

# Split transcript
chunks = split_text(transcript)

# Print total chunks
print(f"Total Chunks: {len(chunks)}")

# Print first chunk
print("\nFirst Chunk:\n")
print(chunks[0])