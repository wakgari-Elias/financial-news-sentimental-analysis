"""
Module: time_series
Analyze time-based trends in financial news data.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid", palette="muted", font_scale=1.1)

def plot_daily_articles(df: pd.DataFrame):
    """
    Plot number of articles published per day.
    """
    df['date_only'] = df['date'].dt.date
    daily_counts = df.groupby('date_only').size()
    plt.figure(figsize=(14,5))
    daily_counts.plot()
    plt.title("Daily Number of Articles Published")
    plt.xlabel("Date")
    plt.ylabel("Number of Articles")
    plt.show()
