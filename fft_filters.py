# https://ipython-books.github.io/101-analyzing-the-frequency-components-of-a-signal-with-a-fast-fourier-transform/
import datetime
import numpy as np
import scipy as sp
import scipy.fftpack
import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("DATASET.CSV")
temp = df.Close
date = df.Date

# NOTE uses annual timeframe, / 365 daily dataset
temp_fft = sp.fftpack.fft(temp)
temp_psd = np.abs(temp_fft) ** 2
fftfreq = sp.fftpack.fftfreq(len(temp_psd), 1. / 365)
# fftfreq = sp.fftpack.fftfreq(len(temp_psd), 1. / 30)
i = fftfreq > 0

# plot signal and
fig, ax = plt.subplots(1, 1, figsize=(8, 4))
ax.plot(fftfreq[i], 10 * np.log10(temp_psd[i]))
ax.set_xlim(0, 5)
ax.set_xlabel('Frequency (1/year)')
ax.set_ylabel('PSD (dB)')

print("highpass")
# cut out frequencies higher than 1 (fundamental)
temp_fft_bis = temp_fft.copy()
temp_fft_bis[np.abs(fftfreq) > 1.1] = 0
temp_slow = np.real(sp.fftpack.ifft(temp_fft_bis))
fig, ax = plt.subplots(1, 1, figsize=(6, 3))
temp.plot(ax=ax, lw=.5)
ax.plot_date(date, temp_slow, '-')
'''
ax.set_xlim(datetime.date(1994, 1, 1),
            datetime.date(2000, 1, 1))
ax.set_xlim(datetime.date(2015, 1, 1),
            datetime.date(2019, 11, 1))
ax.set_ylim(-10, 40)
'''
ax.set_xlabel('Date')
ax.set_ylabel('Mean temperature')

plt.show()

