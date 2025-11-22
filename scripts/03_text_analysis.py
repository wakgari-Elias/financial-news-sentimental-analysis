# 03_text_analysis.py
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF
from scripts.01_data_loading import df

# Preprocessing
text_data = df['headline'].dropna().str.lower()

# TF-IDF Vectorization
vectorizer = TfidfVectorizer(max_df=0.95, min_df=5, stop_words='english', ngram_range=(1,2))
tfidf = vectorizer.fit_transform(text_data)
print("TF-IDF matrix shape:", tfidf.shape)

# NMF Topic Modeling
n_topics = 5
nmf_model = NMF(n_components=n_topics, random_state=42)
nmf_model.fit(tfidf)

# Top words per topic
feature_names = vectorizer.get_feature_names_out()
for idx, topic in enumerate(nmf_model.components_):
    top_words = [feature_names[i] for i in topic.argsort()[:-11:-1]]
    print(f"Topic {idx+1}: {', '.join(top_words)}")

# Assign dominant topic
topic_distribution = nmf_model.transform(tfidf)
df['dominant_topic'] = topic_distribution.argmax(axis=1)

print("\nSample headlines with dominant topics:")
print(df[['headline', 'dominant_topic']].head(10))
