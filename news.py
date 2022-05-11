import os
import requests
from datetime import date, timedelta


news_api_key = os.environ["NEWS_API_KEY"]

TOPIC = "dogecoin"
TODAY = date.today()
YESTERDAY = TODAY - timedelta(days=1)
LANGUAGE = "en"


class NewsFeed:
    """Represents multiple news titles, links and descriptions as a readable form"""
    base_url = "https://newsapi.org/v2/everything"
    news_api_key = os.environ["NEWS_API_KEY"]

    def __init__(self, topic, from_date, to_date, language):
        self.topic = topic
        self.from_date = from_date
        self.to_date = to_date
        self.language = language

    def get(self):
        url = self._build_url()
        articles = self._get_articles(url)

        email_body = ''
        for article in articles:
            email_body += f"{article['title']} \n {article['url']} \n\n {article['description']} \n\n"
        return email_body

    def _get_articles(self, url):
        response = requests.get(url)
        articles = response.json()['articles']
        return articles

    def _build_url(self):
        url = f"{self.base_url}?" \
              f"q={self.topic}&" \
              f"from={self.from_date}&" \
              f"to={self.to_date}&" \
              f"language={self.language}&" \
              f"apiKey={self.news_api_key}"
        return url


if __name__ == "__main__":
    news_feed = NewsFeed(topic=TOPIC, from_date=YESTERDAY, to_date=TODAY, language=LANGUAGE)
    print(news_feed.get())
