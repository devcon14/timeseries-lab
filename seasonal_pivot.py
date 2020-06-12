import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

df = pd.read_csv("DATASET.CSV", parse_dates=True, index_col="datestamp")
category = "doy"

piv = pd.pivot_table(df, index=[category], columns=['year'], values=['close'])
# piv = pd.pivot_table(df, index=['dow'], columns=['week'], values=['close'], fill_value=0)

period_average = piv.fillna(method='ffill')
period_average = period_average.apply(lambda x: np.mean(x), axis=1)
period_average = period_average.reset_index()
period_average.plot(x=category)
plt.show()

piv["period_average"] = period_average[0]
ax = piv.plot(logy=True, legend=False)
plt.show()
