"""
Module: descriptive_stats
Compute basic statistics on financial news data.
"""

import pandas as pd

def headline_length_stats(df: pd.DataFrame) -> pd.Series:
    """
    Compute descriptive statistics for headline lengths.

    Args:
        df (pd.DataFrame): DataFrame containing 'headline' column.

    Returns:
        pd.Series: Descriptive stats (mean, min, max, std) of headline lengths.
    """
    df['headline_length'] = df['headline'].str.len()
    return df['headline_length'].describe()


def articles_per_publisher(df: pd.DataFrame) -> pd.Series:
    """
    Count number of articles per publisher.

    Args:
        df (pd.DataFrame): DataFrame containing 'publisher' column.

    Returns:
        pd.Series: Count of articles per publisher (descending).
    """
    return df['publisher'].value_counts()
