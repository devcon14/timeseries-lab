import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

df = pd.read_csv("DATASET.CSV", parse_dates=True, index_col="Date")
'''preprocess
df['month'] = df.index.month
df['doy'] = df.index.dayofyear
df['week'] = df.index.week
df['dow'] = df.index.weekday_name
df['hour'] = df.index.hour
'''

# pivot automatically does an average ,aggfunc=np.sum
piv = pd.pivot_table(df, index=['Dow'], columns=['Hour'], values=['Range'], fill_value=0)
sns.heatmap(piv)
# piv.plot()

plt.show()