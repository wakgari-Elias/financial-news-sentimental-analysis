import pandas as pd
from src.sentiment import compute_sentiment
from src.merge_datasets import prepare_and_merge
from src.correlation import compute_daily_returns, compute_correlation

news = pd.read_csv("data/raw/raw_analyst_ratings.csv")
stocks = pd.read_csv("data/processed/AAPL_processed.csv")

news = compute_sentiment(news)
merged = prepare_and_merge(news, stocks)
merged = compute_daily_returns(merged)

corr, p = compute_correlation(merged)

print("Correlation:", corr)
print("P-value:", p)

merged.to_csv("data/processed/task3_merged.csv", index=False)
