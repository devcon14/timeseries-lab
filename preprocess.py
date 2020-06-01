import datetime
import pandas as pd
DATAFOLDER = "data"

def normalise_data(data):
    import numpy as np
    # data = np.linalg.norm(data)
    # normalize, do we need to normalize?
    data = (data - np.mean(data)) / np.std(data)
    return data

def detrend(x):
    # TODO check out numpy detrend
    import numpy as np
    n = x.size
    t = np.arange(0, n)
    p = np.polyfit(t, x, 1)         # find linear trend in x
    x_notrend = x - p[0] * t        # detrended x
    return x_notrend

def add_stationary(df, col):
    # [definition and log method](https://www.analyticsvidhya.com/blog/2018/09/non-stationary-time-series-python/)
    import numpy as np
    df["Logx"] = np.log(df[col])
    df["Stationary"] = df["Logx"] - df["Logx"].shift(1)
    del df["Logx"]

def preprocess_frame(df):
    # DATE_COLUMN = "date"
    DATE_COLUMN = "Date"

    # df[DATE_COLUMN] = pd.to_datetime(df[DATE_COLUMN])
    df["Datestamp"] = pd.to_datetime(df[DATE_COLUMN])
    # df = df.set_index(DATE_COLUMN)

    # cryptodatadownload CDD: Timestamps are UTC timezone
    # make all source data UTC, convert to localtime here
    # df["Datestamp"] = df["Datestamp"].dt.tz_localize('utc').dt.tz_convert("Africa/Johannesburg")
    df["Datestamp"] = df["Datestamp"] + datetime.timedelta(hours=2)

    # ensure dates in ascending order, oldest first
    df = df.sort_values(by="Datestamp", ascending=True)

    if "High" in df.columns:
        df["Range"] = df.High - df.Low
    df["Value"] = df["Close"]
    df["Returns"] = df.Close - df.shift(1).Close
    df["PercentChange"] = df.Close.pct_change(1)
    df["AbsPercentChange"] = abs(df.Close.pct_change(1))
    df["DeTrend"] = detrend(df.Close)
    add_stationary(df, "Value")

    df['Year'] = df.Datestamp.dt.year
    df['Month'] = df.Datestamp.dt.month
    df['Doy'] = df.Datestamp.dt.dayofyear
    df['Dom'] = df.Datestamp.dt.day
    df['Week'] = df.Datestamp.dt.week
    # df['Dow'] = df.Datestamp.dt.weekday_name
    df["Dow"] = df.Datestamp.dt.dayofweek
    # long name for Dow
    df['DayName'] = df.Datestamp.dt.day_name()
    df['Hour'] = df.Datestamp.dt.hour
    # use lowercase for postgresql/timescaledb
    df.columns = [x.lower() for x in df.columns]

    # df["Normalised"] = normalise_data(df.Close)
    df["normalised"] = (df.close - df.close.mean()) / df.close.std()
    return df


def load_frame():
    df = pd.read_csv("dataset.csv", parse_dates=["datestamp"])
    df.index = pd.DatetimeIndex(df.datestamp)
    df.index.name = "datestampindex"
    return df


if __name__ == "__main__":
    # df = pd.read_csv("DATASET.CSV", parse_dates=True, index_col="Date")
    df = pd.read_csv("dataset.csv")
    df = preprocess_frame(df)
    print(df.head())
    df.to_csv("dataset.csv")
