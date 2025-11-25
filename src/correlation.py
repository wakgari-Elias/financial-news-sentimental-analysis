import pandas as pd
from scipy.stats import pearsonr

def compute_daily_returns(df):
    df["Daily_Return"] = df["Close"].pct_change()
    return df

def compute_correlation(df):
    df_clean = df.dropna(subset=["Daily_Return", "sentiment"])
    corr, p = pearsonr(df_clean["Daily_Return"], df_clean["sentiment"])
    return corr, p
