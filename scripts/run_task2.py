from src.loader import load_stock_files
from src.indicators import apply_indicators_to_all
from src.analytics import summary_report
from src.utils import save_processed_data

def main():
    print("\n=== Task 2 Pipeline Started ===\n")

    # 1. Load data
    stock_data = load_stock_files()

    # 2. Apply indicators
    stock_data = apply_indicators_to_all(stock_data)

    # 3. Summary output
    summary_report(stock_data)

    # 4. Save processed CSVs
    save_processed_data(stock_data)

    print("\n=== Task 2 Completed Successfully ===")

if __name__ == "__main__":
    main()
