import threading
from queue import Queue
import yt_dlp
import whisper
import requests
from bs4 import BeautifulSoup
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os

nltk.download('punkt')

def download_video(video_url, output_queue):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        }],
        'outtmpl': 'audio.%(ext)s',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(video_url, download=True)
        video_title = info['title']
    output_queue.put(('audio.wav', video_title))

def extract_transcript(input_queue, output_queue):
    audio_file, video_title = input_queue.get()
    model = whisper.load_model("base")
    result = model.transcribe(audio_file)
    transcript = result["text"]
    output_queue.put((transcript, video_title))
    os.remove(audio_file)

def web_scraping(video_title, output_queue):
    search_url = f"https://www.google.com/search?q={video_title}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = []
    for g in soup.find_all('div', class_='g'):
        anchors = g.find_all('a')
        if anchors:
            link = anchors[0]['href']
            if link.startswith('http'):
                try:
                    article_response = requests.get(link, headers=headers, timeout=5)
                    article_soup = BeautifulSoup(article_response.text, 'html.parser')
                    article_text = article_soup.get_text()
                    articles.append((link, article_text))
                except:
                    pass
    output_queue.put(articles)

def similarity_calculation(transcript_queue, articles_queue, output_queue):
    transcript, video_title = transcript_queue.get()
    articles = articles_queue.get()
    
    texts = [transcript] + [article[1] for article in articles]
    vectorizer = TfidfVectorizer().fit_transform(texts)
    cosine_similarities = cosine_similarity(vectorizer[0:1], vectorizer[1:]).flatten()
    
    similar_articles = sorted(zip(articles, cosine_similarities), key=lambda x: x[1], reverse=True)
    output_queue.put((video_title, similar_articles[:3]))  # Return top 3 similar articles
