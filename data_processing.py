import yfinance as yf
import pandas as pd
import sys
from pandas.tseries.offsets import BusinessDay

def get_stock_data(ticker, start_date, end_date, interval):
    """
    Fetches OHLCV data for a given stock and timeframe.
    
    Parameters:
        ticker (str): Stock ticker symbol (e.g. 'AAPL')
        start_date (str): Start date in 'YYYY-MM-DD' format
        end_date (str): End date in 'YYYY-MM-DD' format
        interval (str): Data interval ('1m', '5m', '15m', '1h', '1d', '1wk', etc.)
    """
    data = yf.download(
        tickers=ticker,
        start=start_date,
        end=end_date,
        interval=interval,
        progress=False
    )
    
    if data.empty:
        print("No data found for given inputs.")
        return None
    
    return data


# Example usage
if __name__ == "__main__":
    if len(sys.argv) == 1:
        ticker = input("Enter stock ticker (e.g. AAPL): ").upper()
        start_date = input("Enter start date (YYYY-MM-DD): ")
        end_date = input("Enter end date (YYYY-MM-DD), or 'daily' only start date: ")
        interval = input("Enter interval (1m, 5m, 15m, 1h, 1d, 1wk): ")
    elif len(sys.argv) == 5:
        ticker = sys.argv[1].upper()
        start_date = sys.argv[2]
        end_date = sys.argv[3]
        interval = sys.argv[4]
    else:
        exit("Please provide inputs for stock ticker (e.g. AAPL), " \
        "start date (YYYY-MM-DD), end date (YYYY-MM-DD), "
        "and time interval (1m, 5m, 15m, 1h, 1d, 1wk) respectively")
    
    if end_date.lower() == "daily":
        out_filename_affix = ""
        end_date = pd.to_datetime(start_date) + BusinessDay(1)
    else:
        out_filename_affix = f"_to_{end_date}"

    print("Starting fetch request...")
    df = get_stock_data(ticker, start_date, end_date, interval)
    df.index.tz_convert("US/Eastern")
    print(end_date)
    print(end_date.date())
    if df is not None:
        print(df.head())
        # Optionally save to CSV
        save = input("Save to CSV? (y/n): ")
        if save.lower() == "y":
            out_filename = f"{ticker}_{interval}_{start_date}{out_filename_affix}.csv"
            df.head().to_csv(out_filename)
            print(f"Data saved to {out_filename}")
