import pandas as pd

def prepare_and_merge(news, stocks):
    news["Date"] = pd.to_datetime(news["Date"]).dt.date
    stocks["Date"] = pd.to_datetime(stocks["Date"]).dt.date

    # If multiple news per day → average sentiment later
    daily_news = news.groupby("Date")["sentiment"].mean().reset_index()

    merged = stocks.merge(daily_news, on="Date", how="left")
    merged["sentiment"].fillna(0, inplace=True)

    return merged
