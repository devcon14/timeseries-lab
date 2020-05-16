import pandas as pd


df = pd.read_csv("btc.csv")
df["Close"] = df["PriceUSD"]
# df["Date"] = df["date"]
df = df.rename(columns={"date": "Date"})
"""

# lean hogs front month
df = pd.read_csv("CHRIS-CME_LN1.csv")
df["Close"] = df["Last"]
# spread
# df_2 = pd.read_csv("CHRIS-CME_LN2.csv")
# df["Close"] = df["Close"] - df_2["Last"]
df = df.sort_values("Date")
"""

df = df[pd.notnull(df.Close)]
df.Date = pd.to_datetime(df.Date)
df["year"] = df.Date.dt.year
# daily pct returns
df["returns"] = df.Close / (df.Close - df.Close.shift(1))

#%%
def join_year(df_last_year, current_year):
    dfy = pd.DataFrame({
            # "dates": df[df.year==current_year].date.values,
            "dayofyear": df[df.year==current_year].Date.dt.dayofyear,
            f"price_{current_year}": df[df.year==current_year].returns.values,
        },
        # index=df[df.year==2017].Date.values
    )
    # merged = dfy.merge(df_year, left_on="dates", right_on="dates")
    merged = df_last_year.merge(dfy, on="dayofyear", how="left")
    # merged = df_last_year.merge(dfy, left_on="dayofyear", right_on="dayofyear")
    # merged = dfy.merge(df_year, left_on="dayofyear", right_on="dayofyear")
    merged[f"price_{current_year}"].bfill(inplace=True)
    merged[f"price_{current_year}"].ffill(inplace=True)
    return merged

base_year_n = 2010
df_data_year = {
    "dates": pd.date_range(f"{base_year_n}-01-01", f"{base_year_n}-12-31"),
    # "dates": pd.date_range("2016-01-01", "2017-01-01"),
}
df_data_year["dayofyear"] = range(1, len(df_data_year["dates"])+1)
base_year = pd.DataFrame(df_data_year)
merged = join_year(base_year, base_year_n)
for current_year in range(2011, 2019):
    merged = join_year(merged, current_year)
    # print(len(merged))
# merged = join_year(merged, 2016)
# merged = join_year(merged, 2017)
# merged = join_year(merged, 2018)
merged.tail()
#%%

"""
data = {
    "2017_p": df[df.year==2017].returns.values,
    "2018_p": df[df.year==2018].returns.values,
}
data_index = df[df.year==2016].date
cdf = pd.DataFrame(data, index=data_index)
"""
del merged["dayofyear"]
m_corr = merged.corr(method='pearson')
# absolute correlation
# m_corr = m_corr.apply(lambda x: abs(x))
print(m_corr)
print(m_corr[f"price_{base_year_n}"].mean())

#%%
