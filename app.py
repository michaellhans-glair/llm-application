# app.py
from flask import Flask, request, render_template
from pytube import YouTube
from openai import OpenAI
from transcript_extractor import fetch_transcript  # Importing our custom transcript extraction function
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

app = Flask(__name__)

# Set your OpenAI API key here
client = OpenAI(api_key=api_key)

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
        video_title = "YouTube Title"
        video_thumbnail = yt.thumbnail_url

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

        # Call OpenAI API to summarize the transcript using the new format
        response = client.completions.create(model="gpt-3.5-turbo",
            prompt=prompt_template,
            max_tokens=300,
            temperature=0.7)
        summary = response.choices[0].text.strip()

        return render_template('index.html', video_url=video_url, summary=summary, transcript=transcript_text, 
                               video_title=video_title, video_thumbnail=video_thumbnail)
    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
