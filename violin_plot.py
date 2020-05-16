# http://seaborn.pydata.org/tutorial/categorical.html#categorical-tutorial
import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

df = pd.read_csv("DATASET.CSV", parse_dates=True, index_col="Date")
'''preprocess
df['month'] = df.index.month
df['doy'] = df.index.dayofyear
df['week'] = df.index.week
# 0 = monday, 6 = sunday
# df['dow'] = df.index.dayofweek
df['dow'] = df.index.weekday_name
df['hour'] = df.index.hour
'''

category = "Month"
y_value = "AbsPercentChange"
# swarm, box, boxen, violin
plot_kind = "violin"

ax = sns.catplot(x=category, y=y_value, data=df, kind=plot_kind)
# ax = sns.violin(x=category, y=y_value, data=df)
plt.xticks(rotation=65)
plt.show()