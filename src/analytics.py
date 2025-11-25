def summary_report(stock_data):
    """Print summary of indicators availability."""
    print("\n=== Indicator Summary ===")
    for name, df in stock_data.items():
        cols = list(df.columns)
        print(f"{name}: {cols}")
