import talib as ta
import numpy as np

def apply_basic_indicators(df):
    """Adds SMA, RSI, MACD, and volatility indicators to the dataframe."""

    required_cols = {"Open", "High", "Low", "Close"}
    if not required_cols.issubset(df.columns):
        print("Missing Open, High, Low, Close — indicators skipped.")
        return df

    df["SMA_20"] = ta.SMA(df["Close"], timeperiod=20)
    df["SMA_50"] = ta.SMA(df["Close"], timeperiod=50)
    df["RSI_14"] = ta.RSI(df["Close"], timeperiod=14)

    macd, signal, hist = ta.MACD(
        df["Close"], fastperiod=12, slowperiod=26, signalperiod=9
    )
    df["MACD"] = macd
    df["MACD_signal"] = signal
    df["MACD_hist"] = hist

    # returns + volatility
    df["Return"] = df["Close"].pct_change()
    df["Volatility_20"] = df["Return"].rolling(window=20).std() * np.sqrt(252)

    return df


def apply_indicators_to_all(stock_data):
    """Applies indicators to every stock in the dictionary."""
    for name, df in stock_data.items():
        stock_data[name] = apply_basic_indicators(df)
        print(f"Indicators applied: {name}")

    return stock_data
