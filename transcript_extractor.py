# transcript_extractor.py
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import NoTranscriptFound, VideoUnavailable

def get_video_id(url):
    """
    Extracts YouTube video ID from the given URL.
    """
    try:
        if 'youtube.com' in url:
            return url.split('v=')[-1]
        elif 'youtu.be' in url:
            return url.split('/')[-1]
        else:
            raise ValueError("Invalid YouTube URL")
    except Exception as e:
        print(f"Error extracting video ID: {e}")
        return None

def fetch_transcript(video_url):
    """
    Fetches the transcript of a YouTube video using its URL.
    
    :param video_url: URL of the YouTube video
    :return: Transcript as a string, or an error message
    """
    video_id = get_video_id(video_url)
    if not video_id:
        return "Invalid or unsupported YouTube URL."

    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        transcript_text = ' '.join([item['text'] for item in transcript_list])
        return transcript_text
    except VideoUnavailable:
        return "The video is unavailable or does not exist."
    except NoTranscriptFound:
        return "No transcript found for this video."
    except Exception as e:
        return f"An error occurred while fetching the transcript: {str(e)}"

# Example usage for testing:
if __name__ == "__main__":
    test_url = input("Enter a YouTube video URL: ")
    transcript = fetch_transcript(test_url)
    print("Transcript:\n", transcript)
