# YouTube Video Summarization App

This is a Flask-based web application that generates a brief summary and displays the transcript of a YouTube video. The app leverages **Google's Gemini Language Model API** to generate structured and concise summaries based on the YouTube video transcript.

Important Note: Currently, the deployed website isn't functioning properly because of a library limitation. YouTube somehow blocked the static IP address of Vercel app that tries to hit the YouTube API inside the YouTube Transcription API Library.

![YouTube Summarization Demo](./assets/llm-demo.gif)

## Features

- **Summarizes YouTube videos**: Automatically fetches and summarizes the transcript of a YouTube video.
- **Transcript Display**: Displays the complete transcript of the YouTube video.
- **YouTube Video Embedding**: Embeds the YouTube video for a better visual reference.
- **Markdown Support**: Supports rendering responses that are in Markdown format.

## Tech Stack

- **Backend**: Flask, Python
- **Frontend**: HTML, Bootstrap, JavaScript
- **APIs**: Gemini Language Model API, YouTube Transcript API
- **Markdown Rendering**: Python-Markdown or marked.js (JavaScript)

## Prerequisites

- **Python 3.x**
- **Pip** (Python package installer)
- **Gemini API Key** from Google's Gemini Language Model API
- **YouTube API dependencies**: pytube, youtube-transcript-api

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/michaellhans-glair/llm-application.git
   cd llm-application
   ```

2. **Create a virtual environment** and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:

   Create a file named `.env` in the root of your project directory with the following content:

   ```bash
   GEMINI_API_KEY=your-gemini-api-key
   ```

5. **Run the Flask application**:

   ```bash
   python app.py
   ```

6. **Open your browser** and visit `http://127.0.0.1:5000/`.

## Usage

1. Enter a YouTube video URL into the input field.
2. Click on the **"Summarize"** button.
3. View the video, generated summary, and the transcript on the results page.

## File Structure

```plaintext
.
├── app.py                   # Main Flask app logic
├── youtube_service.py  # Contains functions for fetching transcript and video details
├── requirements.txt         # Project dependencies
├── .env                     # Environment variables (not tracked by Git)
├── templates/
│   └── index.html           # HTML template for the web app
└── README.md                # Project documentation
```
Here is an **Author** section that you can include in your `README.md`:

## Author

**Michael Hans**  
*Software Development Engineer*  

- **GitHub**: [github.com/michaellhans-glair](https://github.com/michaellhans-glair)  
- **LinkedIn**: [linkedin.com/in/michaellhans](https://linkedin.com/in/michaellhans)
