"""
Module: data_loader
Load and preprocess financial news data in a reusable class.
"""

import pandas as pd
from pathlib import Path

class FinancialNewsLoader:
    """
    Class to load financial news data from a CSV and clean it.
    """

    def __init__(self, path="data/raw/raw_analyst_ratings.csv"):
        self.path = Path(path)
        self.expected_cols = ['headline', 'publisher', 'date', 'url', 'stock']

    def load_data(self) -> pd.DataFrame:
        """
        Load CSV into DataFrame and preprocess.

        Returns:
            pd.DataFrame: Cleaned DataFrame with expected columns.
        """
        if self.path.exists():
            df = pd.read_csv(self.path, low_memory=False)
            print(f"Loaded CSV from: {self.path}")
        else:
            print(f"CSV not found at {self.path}. Using empty DataFrame.")
            df = pd.DataFrame(columns=self.expected_cols)

        # Ensure expected columns exist
        for col in self.expected_cols:
            if col not in df.columns:
                df[col] = pd.NA

        # Convert date column to datetime
        df['date'] = pd.to_datetime(df['date'], errors='coerce')

        # Drop rows with missing headlines or dates
        df = df.dropna(subset=['headline', 'date'])
        return df


# Example usage (can remove in production)
if __name__ == "__main__":
    loader = FinancialNewsLoader()
    df = loader.load_data()
    print(df.head())
