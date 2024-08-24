# Tracing Sources of Fake News Video on YouTube

## Description
This Python program aims to find potential sources of content for YouTube videos. It downloads a YouTube video, transcribes its audio, searches for related articles on the web, and calculates the similarity between the video transcript and the found articles.

**Note:** This tool is for educational purposes only. It does not determine the veracity of information or identify "fake news". Always verify information through reliable fact-checking methods.

## Features
- YouTube video download
- Audio transcription using OpenAI's Whisper model
- Web scraping for related articles
- Text similarity calculation

## Prerequisites
- Python 3.7+
- pip (Python package installer)

## Installation

1. Clone this repository:
```
git clone https://github.com/yourusername/youtube-content-source-finder.git
cd youtube-content-source-finder
```
2. Install the required packages:
```
pip install yt-dlp whisper torch requests beautifulsoup4 nltk scikit-learn
```
When prompted, enter the URL of the YouTube video you want to analyze.

## How it Works

1. **Video Download**: Uses yt-dlp to download the audio from the specified YouTube video.
2. **Transcription**: Employs OpenAI's Whisper model to transcribe the audio.
3. **Web Scraping**: Searches Google for articles related to the video title and scrapes their content.
4. **Similarity Calculation**: Uses TF-IDF and cosine similarity to find articles most similar to the video transcript.

## Limitations

- The program uses basic web scraping techniques which may not work for all websites.
- It relies on Google search results, which may have usage limitations.
- The similarity calculation is basic and may not capture all nuances of content similarity.
- This tool does not determine the truthfulness or reliability of content.

## Ethical Considerations

- Respect copyright and fair use laws when using content.
- Be aware of and comply with the terms of service for YouTube and any websites you scrape.
- Use web scraping responsibly and implement rate limiting to avoid overloading servers.

## Future Improvements

- Implement more advanced NLP techniques for better similarity matching.
- Add support for multiple languages.
- Improve error handling and logging.
- Implement a user interface for easier interaction.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.

## Disclaimer

This software is provided for educational purposes only. Users are responsible for using it in compliance with all applicable laws and regulations. The authors are not responsible for any misuse or legal consequences arising from the use of this software.
