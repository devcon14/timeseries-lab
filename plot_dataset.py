import pandas as pd
from matplotlib import pyplot as pl

df = pd.read_csv("DATASET.CSV")

# matplotlib
df[["PercentChange"]].plot()
pl.show()

# plotly studio
import chart_studio.plotly as py
import plotly.graph_objects as go
trace1 = go.Scatter(
    x=df.Date,
    y=df.Close,
    mode='lines',
)
fig = go.Figure(data=[trace1])
py.iplot(fig, filename='simple-plot')


# it looks like I'm unable to bind the plotly webserver locally without admin?
# nice examples of using dash and rangeslider with timeseries
# https://plot.ly/python/time-series/

def cuff():
    import plotly.express as px
    fig = px.line(df, x='Date', y='Close')
    fig.show()

    fig = go.Figure(data=go.Scatter(x=df.Date, y=df.Close))
    fig.show()

    # https://plot.ly/ipython-notebooks/cufflinks/
    import plotly.plotly as py
    import cufflinks as cf
    import pandas as pd
    import numpy as np
    print (cf.__version__)
    # df[["Close"]].iplot()

    # https://dash.plot.ly/?_ga=2.58705066.1204431297.1570091276-22423526.1570091276
