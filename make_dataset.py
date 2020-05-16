import numpy as np
import pandas as pd
# import seaborn as sns
from matplotlib import pyplot as plt
DATAFOLDER = "data"


# get BTC
def get_btc(timeframe="hourly"):
    # coinmetrics
    if False:
        df = pd.read_csv("btc.csv")
        df["Close"] = df["PriceUSD"]
        # df["Date"] = df["date"]
        df = df.rename(columns={"date": "Date"})

    # cryptodatadownload, timestamps are UTC timezone
    # timeframe = "daily"
    # timeframe = "hourly"
    if timeframe == "hourly":
        df = pd.read_csv(f"{DATAFOLDER}/Bitstamp_BTCUSD_1h.csv")
        df["Date"] = df.Date.map(lambda x: x[:13] + ":00 " + x[14:])
    elif timeframe == "daily":
        df = pd.read_csv(f"{DATAFOLDER}/Bitstamp_BTCUSD_d.csv")
    return df

def get_oil():
    # oil
    # CHRIS-ICE_B1, Brent Crude Futures, Continuous Contract on ICE
    # CHRIS-CME_CL1, CME crude light front month
    # can't find west texas futures, maybe look at shanghai oil?

    # FRED-OILPRICE, Spot Oil Price: West Texas Intermediate
    # FRED-IPG211111CSQ, Industrial production crude oil mining
    # FRED-MCOILBRENTEU, Crude Oil Prices: Brent - Europe
    df = pd.read_csv(f"{DATAFOLDER}/CHRIS-CME_CL1.csv")
    df["Close"] = df.Last
    return df

# get hogs
def get_hogs():
    df = pd.read_csv(f"{DATAFOLDER}/CHRIS-CME_LN1.csv")
    df["Close"] = df.Last
    return df

def get_hogs_spread():
    df1 = pd.read_csv(f"{DATAFOLDER}/CHRIS-CME_LN1.csv")
    df2 = pd.read_csv(f"{DATAFOLDER}/CHRIS-CME_LN2.csv")
    df1["Close"] = df1.Last - df2.Last
    return df1

def get_corn_futures():
    # CHRIS-ICE_IW1: wheat continous till 2017 but spikes to 0 repeatedly
    # CHRIS-MGEX_IH1: wheat till 2008 only
    # futures are dirty
    # df = pd.read_csv("CHRIS-MGEX_IC1.csv")
    # df["Close"] = df.Last
    pass

def get_corn():
    df = pd.read_csv(f"{DATAFOLDER}/corn-prices-historical-chart-data.csv")
    df = df.rename(columns={"date": "Date", " value": "Close"})
    return df

def get_wheat():
    df = pd.read_csv(f"{DATAFOLDER}/wheat-prices-historical-chart-data.csv")
    df = df.rename(columns={"date": "Date", " value": "Close"})
    return df

def get_quandl(name):
    if "CHRIS" in name:
        filename = name.replace("/", "-") + ".csv"
        df = pd.read_csv(f"{DATAFOLDER}/" + filename)
        df["Close"] = df.Last
    if "MULTPL" in name:
        filename = name.replace("/", "-") + ".csv"
        df = pd.read_csv(f"{DATAFOLDER}/" + filename)
        df = df.rename(columns={"Value": "Close"})
    return df

# or prep_dataset
def compile_dataset(dataset):
    # hardcode some macrotrends.net
    if dataset == "sp500-10-year-daily-chart.csv":
        df = pd.read_csv(f"{DATAFOLDER}/macrotrends/" + dataset, skiprows=15)
        df = df.rename(columns={"date": "Date", " value": "Close"})
    elif dataset == "bytetree_1d_bitcoin.csv":
        df = pd.read_csv(f"{DATAFOLDER}/" + dataset)
        # df = pd.read_csv("bytetree_1d_bitcoin.csv")
        # df = pd.read_csv("bitcoin.csv")
        # time, t1v|d1v (first Spend|USD), hgt (block height), dif (difficulty), gen (coins generated)
        # txv (transaction value)
        df = df.rename(columns={"date": "Date", "dpr": "Close"})
    elif dataset == "bytetree_1h_bitcoin.csv":
        df = pd.read_csv(f"{DATAFOLDER}/" + dataset)
        df["Date"] = pd.to_datetime(df.date + ' ' + df.time)
        df = df.rename(columns={"dpr": "Close"})
    elif dataset == "Bitstamp_BTCUSD_1h.csv":
        df = get_btc("hourly")
    elif dataset == "Bitstamp_BTCUSD_d.csv":
        df = get_btc("daily")
    elif "CHRIS" in dataset:
        df = get_quandl(dataset)
    elif "MULTPL" in dataset:
        df = get_quandl(dataset)

    from preprocess import preprocess_frame
    df = preprocess_frame(df)
    df.to_csv("DATASET.CSV")

    '''
    from matplotlib import pyplot as pl
    df[["Close"]].plot()
    pl.show()
    '''
    return df

def compile_old(SOURCE):
    # TIMEFRAME = "hourly"
    TIMEFRAME = "daily"
    if SOURCE == "BTC":
        df = get_btc(TIMEFRAME)
    elif SOURCE == "HOGS":
        df = get_hogs()
    elif SOURCE == "HOGS_SPREAD":
        df = get_hogs_spread()
    elif SOURCE == "CORN":
        df = get_corn()
    elif SOURCE == "WHEAT":
        df = get_wheat()
    elif SOURCE == "OIL":
        df = get_oil()
    from preprocess import preprocess_frame
    df = preprocess_frame(df)
    '''
    # preprocess
    df["Date"] = pd.to_datetime(df.Date)
    df = df.set_index("Date")
    # ensure dates in ascending order, oldest first
    df = df.sort_values(by="Date", ascending=True)
    if "High" in df.columns:
        df["Range"] = df.High - df.Low
    df["Value"] = df["Close"]
    df["Returns"] = df.Close - df.shift(1).Close
    df["PercentChange"] = df.Close.pct_change(1)
    print(df.head())
    '''
    df.to_csv("DATASET.CSV")

    from matplotlib import pyplot as pl
    df[["Close"]].plot()
    pl.show()

if __name__ == "__main__":
    SOURCE = "BTC"
    # compile_old(SOURCE)

    compile_dataset("sp500-10-year-daily-chart.csv")
    # compile_dataset("CHRIS/CME_SP1")
    # compile_dataset("MULTPL/SP500_REAL_PRICE_MONTH")
    # compile_dataset("bytetree_1d_bitcoin.csv")
    # compile_dataset("CDD Bitstamp Hourly")
