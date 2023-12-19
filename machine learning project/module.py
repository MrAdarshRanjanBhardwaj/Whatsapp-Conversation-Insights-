from urlextract import URLExtract

from wordcloud import WordCloud
import pandas as pd
from collections import Counter
import re


extract = URLExtract()
from textblob import TextBlob


def analyze_sentiment(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    messages = ' '.join(df['message'].tolist())
    from nltk.sentiment.vader import SentimentIntensityAnalyzer
    sentiments = SentimentIntensityAnalyzer()
    df["positive"] = [sentiments.polarity_scores(i)["pos"] for i in data["Message"]]
    df["negative"] = [sentiments.polarity_scores(i)["neg"] for i in data["Message"]]
    df["neutral"] = [sentiments.polarity_scores(i)["neu"] for i in data["Message"]]

    x = sum(df["positive"])
    y = sum(df["negative"])
    z = sum(df["neutral"])

    def score(a, b, c):
        if (a > b) and (a > c):
            print("Positive ")
        if (b > a) and (b > c):
            print("Negative")
        if (c > a) and (c > b):
            print("Neutal")

    return score(x, y, z)
