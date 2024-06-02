import sys
import webbrowser

urls = {
    "work": ["https://www.replit.com", "https://www.github.com", "https://gemini.google.com"],
    "entertainment": ["https://www.disneyplus.com", "https://www.netflix.com", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"]
}

def open_webpages(urls):
    for url in urls:
        webbrowser.open(url)

open_webpages(urls["entertainment"])

if __name__ == "__main__":
    set_name = sys.argv[1]
    urls = urls[set_name]
    open_webpages(urls)
