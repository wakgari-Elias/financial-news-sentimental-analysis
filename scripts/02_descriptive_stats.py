# 02_descriptive_stats.py
import pandas as pd
from scripts.01_data_loading import df

# Headline length statistics
df['headline_length'] = df['headline'].str.len()
print("Headline length stats:")
print(df['headline_length'].describe())

# Articles per publisher
publisher_counts = df['publisher'].value_counts()
print("\nTop 10 publishers by number of articles:")
print(publisher_counts.head(10))

# Articles over time
df['date_only'] = df['date'].dt.date
daily_counts = df.groupby('date_only').size()
print("\nDaily article counts:")
print(daily_counts.head(10))
