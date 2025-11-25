import os

def save_processed_data(stock_data, out_dir="data/processed"):
    """Saves processed stock data."""
    os.makedirs(out_dir, exist_ok=True)

    for name, df in stock_data.items():
        df.to_csv(f"{out_dir}/{name}_processed.csv", index=False)
        print(f"Saved processed: {name}")
