import os
import glob
import pandas as pd

RAW_DATA_PATH = "data/raw"

def load_stock_files():
    """Loads all CSV stock files from the raw data folder."""
    file_paths = glob.glob(os.path.join(RAW_DATA_PATH, "*.csv"))
    stock_data = {}

    print(f"Found {len(file_paths)} CSV files.\n")

    for path in file_paths:
        name = os.path.basename(path).replace(".csv", "").upper()
        df = pd.read_csv(path)

        # Standardize column names
        df.columns = [col.capitalize() for col in df.columns]

        # Convert Date to datetime
        if "Date" in df.columns:
            df["Date"] = pd.to_datetime(df["Date"])

        stock_data[name] = df
        print(f"Loaded: {name}")

    return stock_data
