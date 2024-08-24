from src import *

def main():
    video_url = input("Enter YouTube video URL: ")
    
    video_queue = Queue()
    transcript_queue = Queue()
    articles_queue = Queue()
    result_queue = Queue()

    download_thread = threading.Thread(target=download_video, args=(video_url, video_queue))
    transcript_thread = threading.Thread(target=extract_transcript, args=(video_queue, transcript_queue))
    scraping_thread = threading.Thread(target=web_scraping, args=(transcript_queue.get()[1], articles_queue))
    similarity_thread = threading.Thread(target=similarity_calculation, args=(transcript_queue, articles_queue, result_queue))

    download_thread.start()
    transcript_thread.start()
    scraping_thread.start()
    similarity_thread.start()

    download_thread.join()
    transcript_thread.join()
    scraping_thread.join()
    similarity_thread.join()

    video_title, similar_articles = result_queue.get()
    print(f"Results for video: {video_title}")
    for i, (article, similarity) in enumerate(similar_articles, 1):
        print(f"{i}. {article[0]} (Similarity: {similarity:.2f})")

if __name__ == "__main__":
    main()
