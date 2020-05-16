import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

# block count price divergence?
# QUANDL:BCHAIN/MIREV, https://www.tradingview.com/symbols/QUANDL-BCHAIN/MIREV/

# get BTC
def get_btc():
    df = pd.read_csv("btc.csv")
    df["Close"] = df["PriceUSD"]
    # df["Date"] = df["date"]
    df = df.rename(columns={"date": "Date"})
    return df

# https://towardsdatascience.com/time-series-in-python-part-2-dealing-with-seasonal-data-397a65b74051
if __name__ == "__main__":
    df = get_btc()
    # df[["Close"]].plot()
    # plt.show()

    def EDA():
        # https://towardsdatascience.com/p-value-explained-simply-for-data-scientists-4c0cd7044f14?source=post_recirc---------2------------------
        # https://towardsdatascience.com/exploring-your-data-with-just-1-line-of-python-4b35ce21a82d
        import pandas_profiling
        # df.profile_report()
        profile = df.profile_report(title='Pandas Profiling Report')
        profile.to_file(output_file="output.html")
        # plt.show()
    # EDA()

    # https://knect365.com/quantminds/article/3e30d9d2-a6c4-4978-8c1c-0b39662ddef8/volatility-seasonality-of-bitcoin-prices
    def season_decompose(df):
        from statsmodels.tsa.seasonal import seasonal_decompose
        df = df.fillna(method='bfill')
        series = pd.Series(df.Close)
        result = seasonal_decompose(series, model='additive', freq=14)
        result.plot()
        plt.show()
    season_decompose(df)