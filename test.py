# Import transcript function
from src.transcript import get_transcript

# YouTube video URL
url = "https://youtu.be/tkZmtsNPdHc?si=3sD88cMRnJ5OY9dC"

# Fetch transcript
transcript = get_transcript(url)

# Print first 1000 characters
print(transcript[:1000])