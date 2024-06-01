import requests
from bs4 import BeautifulSoup
import os
import json

def scrape_ai_news():
    url = "https://www.example.com/ai-news"  # Placeholder URL
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    articles = []
    for item in soup.select('.news-item'):
        title = item.select_one('.news-title').text
        summary = item.select_one('.news-summary').text
        link = item.select_one('a')['href']
        articles.append({"title": title, "summary": summary, "link": link})

    if not os.path.exists('data'):
        os.makedirs('data')

    with open('data/ai_news.json', 'w') as f:
        json.dump(articles, f, indent=4)

if __name__ == "__main__":
    scrape_ai_news()
