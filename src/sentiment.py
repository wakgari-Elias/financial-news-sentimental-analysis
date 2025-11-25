import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def compute_sentiment(df):
    df["sentiment"] = df["Headline"].astype(str).apply(
        lambda x: analyzer.polarity_scores(x)["compound"]
    )
    return df
