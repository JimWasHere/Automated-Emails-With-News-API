import yagmail
import pandas
import os
from datetime import date, timedelta
from news import NewsFeed


TODAY = date.today()
YESTERDAY = TODAY - timedelta(days=1)
LANGUAGE = "en"
email_username = os.environ['GMAIL_ADDRESS']
gmail_password = os.environ["GMAIL_PASSWORD"]

df = pandas.read_csv("emails.csv")


def send_email():
    news_feed = NewsFeed(topic=row['interest'], from_date=YESTERDAY, to_date=TODAY, language=LANGUAGE)
    email = yagmail.SMTP(user=email_username, password=gmail_password)
    email.send(to=row['email'],
               subject=f"Your {row['interest']} email for the day.",
               contents=f"Hi {row['name']}\n See what's going on with {row['interest']} \n{news_feed.get()}\n\n")


for index, row in df.iterrows():
    send_email()
