import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

SOURCE = "BTC"
df = pd.read_csv("DATASET.CSV", parse_dates=True, index_col="Date")
# df["Date"] = pd.to_datetime(df.Date)
# df = df.set_index("Date")


def plot_difficulty():
    fig, axes = plt.subplots(nrows=3, ncols=1, sharex=True)
    df[["Close"]].plot(ax=axes[0])
    # df[["BlkCnt"]].plot(ax=axes[1], linewidth=2, color='r', linestyle='dashed')
    df[["BlkCnt"]].plot(ax=axes[1])
    df[["DiffMean"]].plot(ax=axes[2])
    # 'AdrActCnt', 'BlkSizeByte'

if SOURCE == "BTC":
    # plot_difficulty()
    pass

# http://atedstone.github.io/pandas-plot-seasons-time-series/
# https://pbpython.com/pandas-pivot-table-explained.html
'''preprocess
df['doy'] = df.index.dayofyear
df['dow'] = df.index.dayofweek
df['year'] = df.index.year
df['week'] = df.index.week
'''
# piv = pd.pivot_table(df, index=['doy'], columns=['year'], values=['Close'])
# piv = pd.pivot_table(df, index=['dow'], columns=['week'], values=['Close'], fill_value=0)
piv = pd.pivot_table(df, index=['Dow'], columns=['Week'], values=['Close'], fill_value=0)

period_average = piv.fillna(method='ffill')
# period_average = piv.fillna(method='pad')
period_average = period_average.apply(lambda x: np.mean(x), axis=1)
period_average = period_average.reset_index()
# period_average.plot(x='doy')
period_average.plot(x='Dow')

piv["period_average"] = period_average[0]
# yearly plot
'''

## generate the sequence with a step of 100 milliseconds
df_times = pd.date_range(t0, t1, freq = '100L', tz= "UTC")

# piv["date_range"] = pd.date_range("2019-01-01", "2019-12-31")
piv["date_range"] = pd.date_range("2019-01-01", "2020-01-01")
piv.plot(logy=True, legend=True, x="date_range")
'''

'''
# weekly plot
'''
ax = piv.plot(logy=True, legend=False)
# ax.set_xticks(piv.index)
# ax.set_xticklabels(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"], rotation=0)

plt.show()
