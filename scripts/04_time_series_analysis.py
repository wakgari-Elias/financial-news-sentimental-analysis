# 04_time_series_analysis.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scripts.01_data_loading import df

sns.set(style="whitegrid", palette="muted", font_scale=1.1)

df['date'] = pd.to_datetime(df['date'], errors='coerce')
df['date_only'] = df['date'].dt.date

# Daily publication frequency
daily_counts = df.groupby('date_only').size()
plt.figure(figsize=(14,5))
daily_counts.plot()
plt.title("Daily Number of Articles Published")
plt.xlabel("Date")
plt.ylabel("Number of Articles")
plt.show()

# Monthly trends
df['month'] = df['date'].dt.to_period('M')
month_counts = df.groupby('month').size()
plt.figure(figsize=(12,5))
month_counts.plot(kind='bar', color='teal')
plt.title("Articles Published Per Month")
plt.xlabel("Month")
plt.ylabel("Number of Articles")
plt.show()

# Weekday trends
df['weekday'] = df['date'].dt.day_name()
weekday_order = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
weekday_counts = df['weekday'].value_counts().reindex(weekday_order)
plt.figure(figsize=(10,5))
weekday_counts.plot(kind='bar', color='coral')
plt.title("Articles Published Per Weekday")
plt.xlabel("Weekday")
plt.ylabel("Number of Articles")
plt.show()

# Hourly trends
df['hour'] = df['date'].dt.hour
hourly_counts = df.groupby('hour').size()
plt.figure(figsize=(10,5))
hourly_counts.plot(kind='bar', color='purple')
plt.title("Articles Published by Hour of Day (UTC)")
plt.xlabel("Hour")
plt.ylabel("Number of Articles")
plt.show()
