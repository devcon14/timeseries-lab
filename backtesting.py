import numpy as np
from plotly.subplots import make_subplots
import plotly.graph_objects as go


def plot_backtest(df):
    # my method
    if "BUY" in df.columns:
        df['Holdings'] = np.where(df['BUY'], 1, None)
    if "SELL" in df.columns:
        df['Holdings'] = np.where(df['SELL'], -1, df['Holdings'])
    df.Holdings = df.Holdings.fillna(method="ffill")
    # df.Holdings = df.Holdings.cumsum()
    df['Rets'] = df.Holdings * df.PercentChange
    # print (df.Holdings)

    # returns = df['Rets'].dropna().cumsum()
    returns = df['Rets'].cumsum()

    # import plotly.express as px
    # fig = make_subplots(rows=2, cols=2, shared_xaxes=True)
    fig_a = go.Figure()
    fig_a.add_scatter(x=df.Date, y=df.Holdings, name="Holdings")
    fig_a.add_scatter(x=df.Date, y=returns, name="Returns")

    fig_b = go.Figure()
    fig_b.add_scatter(x=df.Date, y=df.Close, mode="lines", name="Close")
    # fig.add_scatter(x=df.Date, y=df.MA, mode="lines", name="MA", row=2, col=1)
    if "BUY" in list(df.columns):
        buys = df[df.BUY]
        fig_b.add_scatter(x=buys.Date, y=buys.Close, mode="markers", marker=dict(size=10, symbol=5, color="green"), name="Buys")
    if "SELL" in list(df.columns):
        sells = df[df.SELL]
        fig_b.add_scatter(x=sells.Date, y=sells.Close, mode="markers", marker=dict(size=10, symbol=6, color="red"), name="Sells")
    fig_b.update_yaxes(type="log")
    # fig.update_yaxes(type="log", row=2, col=1)
    # fig.update_layout(yaxis_type="log", row=2, col=1)
    # fig.show()
    return fig_a, fig_b


def st_buy_hold(df):
    df['BUY'] = False
    df.loc[0, 'BUY'] = True


def st_ma(df):
    # https://www.pythonforfinance.net/2017/02/21/intraday-stock-mean-reversion-trading-backtest-in-python-with-short-selling/
    df['MA'] = df['Close'].rolling(window=200).mean()
    # df['Stdev'] = df['Close'].rolling(window=90).std()

    #create a column which holds a TRUE value if the gap down from previous day's low to next 
    #day's open is larger than the 90 day rolling standard deviation
    df['Buy1'] = df['Close'] < df['High'].shift(1)
    df['Buy2'] = df['Close'] > df['MA']
    df['Sell1'] = df['Close'] > df['Low'].shift(1)
    df['Sell2'] = df['Close'] < df['MA']
    df['BUY'] = df['Buy1'] & df['Buy2']
    df['SELL'] = df['Sell1'] & df['Sell2']
    # df['SELL'] = 0


if __name__ == "__main__":
    import pandas as pd
    df = pd.read_csv("DATASET.CSV")

    # st_ma(df)
    st_buy_hold(df)
    df["PercentChange"] = df.Close.pct_change()
    fig_a, fig_b = plot_backtest(df)
    # fig = make_subplots(rows=2, cols=2, shared_xaxes=True)
    fig_a.show()
    fig_b.show()
