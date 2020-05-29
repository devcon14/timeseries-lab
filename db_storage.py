# pip install psycopg2
# https://stackoverflow.com/questions/33813815/how-to-read-a-parquet-file-into-pandas-dataframe
# SELECT create_hypertable('dataset', 'Date', migrate_data => true);
# https://docs.timescale.com/latest/using-timescaledb/reading-data
# select date_trunc('week', "Date") as week, COUNT(*), AVG("Close") from dataset group by "week" order by "week";
# select time_bucket('2 days', "Date") TwoDays, AVG("Close"), Last("Close", "Date") as close, First("Close", "Date") as open, MAX("Close") as high, MIN("Close") as low from dataset group by TwoDays ORDER BY TwoDays DESC;
# select time_bucket('2 days', "Date") TwoDays, first("Open", "Date") as open, max("High") as high, min("Low") as low, last("Close", "Date") as close, SUM("Volume USD") As volume from bitstamp group by TwoDays;
TIMESCALE_PWD = "password"
TABLE_NAME = "bitstamp_1h"
DATE_FIELD = "Date"

import sqlalchemy
import pandas as pd

# df = pd.read_csv("DATASET.CSV", parse_dates=["Date"])
# df = pd.read_csv(".\data\Bitstamp_BTCUSD_d.csv", parse_dates=["Date"])
df = pd.read_csv(".\data\Bitstamp_BTCUSD_1h.csv", parse_dates=[DATE_FIELD])
print (df)

engine = sqlalchemy.create_engine(f"postgresql://postgres:{TIMESCALE_PWD}@localhost/tutorial")
conn = engine.connect()
df.to_sql(TABLE_NAME, con=conn, if_exists="replace") # append

res = conn.execute(f"SELECT create_hypertable({TABLE_NAME}, '{DATE_FIELD}', migrate_data => true)")
print(res)