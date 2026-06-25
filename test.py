# Import transcript function
from src.transcript import get_transcript

# YouTube video URL
url = "https://www.youtube.com/watch?v=aircAruvnKk"

# Fetch transcript
transcript = get_transcript(url)

# Print first 1000 characters
print(transcript[:1000])