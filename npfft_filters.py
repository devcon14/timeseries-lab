# https://stackoverflow.com/questions/15382076/plotting-power-spectrum-in-python
# https://stackoverflow.com/questions/25735153/plotting-a-fast-fourier-transform-in-python
import numpy as np
import pylab as pl
from numpy import fft
import pandas as pd
import matplotlib.pyplot as plt

def detrend(x):
    n = x.size
    t = np.arange(0, n)
    p = np.polyfit(t, x, 1)         # find linear trend in x
    x_notrend = x - p[0] * t        # detrended x
    return x_notrend

def fill_forward(values, dates):
    from datetime import timedelta
    # project forward
    filler_values = [float(values[-1:])] * 365
    projected_values = np.concatenate((values, filler_values))
    start = pd.to_datetime(dates.iloc[-1]) + timedelta(days=1)
    end = pd.to_datetime(dates.iloc[-1]) + timedelta(days=365)
    filler_dates = pd.date_range(start, end)
    projected_dates = np.concatenate((dates, filler_dates))
    df_dates = pd.concat([pd.Series(dates), pd.Series(filler_dates)])
    df_dates = pd.DatetimeIndex(df_dates)
    # return projected_values, projected_dates
    pd.DataFrame({"Close": projected_values}, index=df_dates).plot()
    plt.show()
    return projected_values

SIGNAL_FIELD = "Close"
df = pd.read_csv("DATASET.CSV")
# df[SIGNAL_FIELD].plot()
values = df[SIGNAL_FIELD]
dates = df.Date
# projected_values = values
# projected_values = fill_forward(values, dates)
projected_values = detrend(values)
# dates = pd.concat([dates, pd.date_range()])
pd.DataFrame({"CloseStat": projected_values}).plot()
plt.show()

freq_domain = np.fft.fft(projected_values)
amp = np.abs(freq_domain)
amp = amp[:int(len(amp)/2)]
freq_df = pd.DataFrame({"amplitude": amp}).plot()
plt.show()

'''
ps = np.abs(np.fft.fft(df.Close))**2
time_step = 1 / 30
freqs = np.fft.fftfreq(len(df), time_step)
idx = np.argsort(freqs)
plt.plot(freqs[idx], ps[idx])
'''

'''
The input should be ordered in the same way as is returned by fft, i.e.,

a[0] should contain the zero frequency term,
a[1:n//2] should contain the positive-frequency terms,
a[n//2 + 1:] should contain the negative-frequency terms, in increasing order starting from the most negative frequency.
For an even number of input points, A[n//2] represents the sum of the values at the positive and negative Nyquist frequencies, as the two are aliased together. See numpy.fft for details.
'''
# lowpass
low = 130
high = 140
important_freq = freq_domain
# important_freq[:low:-1] = 0
# important_freq[high:] = 0

n = len(freq_domain)
# freq_domain[n//2 + 1:] = 0
important_freq = np.zeros(n)
for i_freq in [49, 14]:
    important_freq[i_freq] = freq_domain[i_freq]
    # smoothed_values = np.real(np.fft.ifft(important_freq))
    # plt.plot(smoothed_values)

smoothed_values = np.real(np.fft.ifft(important_freq))
plt.plot(projected_values)
plt.plot(smoothed_values)
# df["Smoothed"] = smoothed_values
# df[[projected_values, "Smoothed"]].plot()

plt.show()