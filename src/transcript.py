# Import transcript API
from youtube_transcript_api import YouTubeTranscriptApi

# Import URL parsing utilities
from urllib.parse import urlparse, parse_qs


# Extract video ID from a YouTube URL
from urllib.parse import urlparse, parse_qs

def extract_video_id(url):

    # Handle short youtu.be URLs
    if "youtu.be" in url:
        return url.split("/")[-1].split("?")[0]

    # Handle youtube.com URLs
    query_params = parse_qs(urlparse(url).query)

    return query_params["v"][0]


# Fetch transcript from a YouTube video
def get_transcript(video_url):

    # Extract video ID from URL
    video_id = extract_video_id(video_url)

    # Create transcript API instance
    ytt_api = YouTubeTranscriptApi()

    # Fetch transcript data
    transcript_data = ytt_api.fetch(
        video_id,
        languages=["en", "hi"]
    )

    # Combine transcript snippets into a single string
    transcript_text = " ".join(snippet.text for snippet in transcript_data)

    # Return transcript text
    return transcript_text