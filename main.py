import pandas as pd
from pprint import pprint
import streamlit as st
import talib
import yfinance as yf



def get_sp500_tickers() -> tuple[list[str], dict[str, str]]:
    """
    Load all S&P 500 tickers into a DataFrame.
    """

    # Add headers
    headers = {
        'User-Agent': 
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    df = pd.read_html("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies", 
                      storage_options=headers)[0]
    tickers = df["Symbol"].tolist()
    tickers_dict = dict(zip(df["Symbol"], df["Security"]))
    return tickers, tickers_dict


def main():
    """
    Main function to execute the primary logic of the script.
    """
    tickers = get_sp500_tickers()
    pprint(tickers)
    return tickers


if __name__ == "__main__":
    main()
