"""
Module: text_analysis
Run basic NLP / topic modeling on financial news headlines.
"""

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF

def extract_topics(df: pd.DataFrame, n_topics=5, n_top_words=10) -> pd.DataFrame:
    """
    Perform TF-IDF vectorization and NMF topic modeling.

    Args:
        df (pd.DataFrame): DataFrame containing 'headline' column.
        n_topics (int): Number of topics to extract.
        n_top_words (int): Top words to display per topic.

    Returns:
        pd.DataFrame: Original df with dominant topic column.
    """
    text_data = df['headline'].dropna().str.lower()

    vectorizer = TfidfVectorizer(
        max_df=0.95,
        min_df=5,
        stop_words='english',
        ngram_range=(1,2)
    )
    tfidf = vectorizer.fit_transform(text_data)

    nmf_model = NMF(n_components=n_topics, random_state=42)
    nmf_model.fit(tfidf)

    feature_names = vectorizer.get_feature_names_out()
    for idx, topic in enumerate(nmf_model.components_):
        top_words = [feature_names[i] for i in topic.argsort()[:-n_top_words-1:-1]]
        print(f"Topic {idx+1}: {', '.join(top_words)}")

    topic_distribution = nmf_model.transform(tfidf)
    df['dominant_topic'] = topic_distribution.argmax(axis=1)
    return df
