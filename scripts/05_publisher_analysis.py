# 05_publisher_analysis.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re
from scripts.01_data_loading import df

sns.set(style="whitegrid", palette="muted", font_scale=1.1)

# Articles per publisher
publisher_counts = df['publisher'].value_counts()
print("Top 10 publishers by number of articles:")
print(publisher_counts.head(10))

plt.figure(figsize=(12,6))
sns.barplot(x=publisher_counts.head(20).values, y=publisher_counts.head(20).index, palette="viridis")
plt.title("Top 20 Publishers by Article Count")
plt.xlabel("Number of Articles")
plt.ylabel("Publisher")
plt.show()

# Extract domains if publisher is email
def extract_domain(publisher):
    if pd.isna(publisher):
        return None
    match = re.search(r'@([\w\.-]+)', publisher)
    return match.group(1) if match else publisher

df['publisher_domain'] = df['publisher'].apply(extract_domain)
domain_counts = df['publisher_domain'].value_counts()
print("\nTop 10 publisher domains:")
print(domain_counts.head(10))

plt.figure(figsize=(12,5))
sns.barplot(x=domain_counts.head(10).values, y=domain_counts.head(10).index, palette="coolwarm")
plt.title("Top 10 Publisher Domains by Article Count")
plt.xlabel("Number of Articles")
plt.ylabel("Domain / Publisher")
plt.show()
