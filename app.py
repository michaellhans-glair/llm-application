# app.py
from flask import Flask, request, render_template
from pytube import YouTube
from youtube_service import fetch_transcript
from dotenv import load_dotenv
import os
import requests
import markdown

# Load environment variables from .env file
load_dotenv()
app = Flask(__name__)
gemini_api_key = os.getenv('GEMINI_API_KEY')
GEMINI_API_ENDPOINT = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent"

def get_gemini_completion(prompt):
    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    params = {
        "key": gemini_api_key
    }

    response = requests.post(GEMINI_API_ENDPOINT, headers=headers, json=data, params=params)

    if response.status_code == 200:
        # Extract the generated text content from the response
        try:
            candidates = response.json().get("candidates", [])
            if candidates:
                # Extract the text from the first candidate's content
                markdown_content = candidates[0].get("content", {}).get("parts", [])[0].get("text", "").strip()
                # Convert Markdown to HTML using the markdown library
                return markdown.markdown(markdown_content)
            else:
                return "No summary generated."
        except (KeyError, IndexError, TypeError):
            return "Unexpected response format from Gemini API."
    else:
        return f"Gemini API error: {response.status_code} - {response.text}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    video_url = request.form['video_url']
    top = 5  # You can adjust this value or make it dynamic
    try:
        # Extract the video ID from the URL and fetch video details using pytube
        yt = YouTube(video_url)

        # Use the fetch_transcript function from transcript_extractor.py to get the transcript
        transcript_text = fetch_transcript(video_url)

        if "error" in transcript_text.lower():
            return render_template('index.html', error=transcript_text)  # Display error if transcript fetching fails

        # Define the summarization prompt template
        prompt_template = f"""
        Summarize the following YouTube video transcript:

        {transcript_text}

        Please provide:
        1. A brief overview of the video's main topic or theme.
        2. Identify the speakers.
        3. The top {top} most important points or insights presented, with a short explanation for each.
        4. Any notable quotes or statements made by the speaker(s).
        5. Key takeaways or conclusions from the video.

        Your response should be well-structured and easy to read.
        """

        # Call the new get_gemini_completion function to summarize the transcript
        summary = get_gemini_completion(prompt_template)
        print(video_url)
        print(summary)

        return render_template('index.html', video_url=video_url, summary=summary, transcript=transcript_text)
    
    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)