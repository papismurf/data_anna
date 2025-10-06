import pandas as pd
from pprint import pprint
import talib


def get_sp500_tickers() -> tuple[list[str], dict[str, str]]:
    """
    Load all S&P 500 tickers into a DataFrame.
    """

    # Add headers
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    df = pd.read_html(
        "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies",
        storage_options=headers,
    )[0]
    tickers = df["Symbol"].tolist()
    tickers_dict = dict(zip(df["Symbol"], df["Security"]))
    return tickers, tickers_dict


indicators = [
    "Exponential Moving Average",
    "Volume Weighted Average Price",
    "Relative Strength Index",
]


def attach_indicator(indicator: str, data: pd.DataFrame) -> pd.DataFrame:
    """
    Apply the selected technical indicator to the DataFrame.
    """
    if indicator == "Exponential Moving Average":
        ema = None
        ema = talib.EMA(data["Close"], timeperiod=20)
        return pd.DataFrame({"Close": data["Close"], "EMA": ema})
    if indicator == "Volume Weighted Average Price":
        vwap = None
        vwap = talib.WMA(data["Close"], timeperiod=20)
        return pd.DataFrame({"Close": data["Close"], "VWAP": vwap})
    if indicator == "Relative Strength Index":
        rsi = None
        rsi = talib.RSI(data["Close"], timeperiod=14)
        return pd.DataFrame({"Close": data["Close"], "RSI": rsi})


def main():
    """
    Main function to execute the primary logic of the script.
    """
    tickers = get_sp500_tickers()
    pprint(tickers)
    return tickers


if __name__ == "__main__":
    main()
