# 01_data_loading.py
import pandas as pd
from pathlib import Path

data_path = Path("data/raw/raw_analyst_ratings.csv")
expected_cols = ['headline', 'publisher', 'date', 'url', 'stock']

if data_path.exists():
    df = pd.read_csv(data_path, low_memory=False)
    print(f"Loaded CSV from: {data_path}")
else:
    print(f"CSV not found at {data_path}. Using empty DataFrame.")
    df = pd.DataFrame(columns=expected_cols)

# Ensure required columns exist
for col in expected_cols:
    if col not in df.columns:
        df[col] = pd.NA

# Convert 'date' column to datetime
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Drop rows with missing headlines or dates
df = df.dropna(subset=['headline', 'date'])

print(f"Data ready: {len(df)} rows, columns: {list(df.columns)}")
