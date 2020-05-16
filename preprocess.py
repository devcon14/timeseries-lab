import pandas as pd

def normalise_data(data):
    import numpy as np
    #normalize, do we need to normalize?
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

def preprocess_frame(df):
    df["Date"] = pd.to_datetime(df.Date)
    df = df.set_index("Date")
    # ensure dates in ascending order, oldest first
    df = df.sort_values(by="Date", ascending=True)
    if "High" in df.columns:
        df["Range"] = df.High - df.Low
    df["Value"] = df["Close"]
    df["Returns"] = df.Close - df.shift(1).Close
    df["PercentChange"] = df.Close.pct_change(1)
    df["AbsPercentChange"] = abs(df.Close.pct_change(1))
    df["DeTrend"] = detrend(df.Close)
    df["Normalised"] = normalise_data(df.Close)

    df['Year'] = df.index.year
    df['Month'] = df.index.month
    df['Doy'] = df.index.dayofyear
    # df['Dom'] = df.index.day
    df['Week'] = df.index.week
    # df['Dow'] = df.index.weekday_name
    # long name for Dow
    df['DayName'] = df.index.day_name()
    df['Hour'] = df.index.hour
    return df


if __name__ == "__main__":
    # df = pd.read_csv("DATASET.CSV", parse_dates=True, index_col="Date")
    df = pd.read_csv("DATASET.CSV")
    df = preprocess_frame(df)
    print(df.head())
    df.to_csv("DATASET.CSV")
