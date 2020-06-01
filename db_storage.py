# CREATE DATABASE trading;
# docker exec -it timescaledb psql -U postgres

# pip install psycopg2
# https://stackoverflow.com/questions/33813815/how-to-read-a-parquet-file-into-pandas-dataframe
# SELECT create_hypertable('dataset', 'Date', migrate_data => true);
# https://docs.timescale.com/latest/using-timescaledb/reading-data
# select date_trunc('week', "Date") as week, COUNT(*), AVG("Close") from dataset group by "week" order by "week";

# select time_bucket('12 hour', "Date") datestamp, Last("Close", "Date") as close, First("Close", "Date") as open, MAX("Close") as high, MIN("Close") as low, SUM("Volume") as volume from bitmex_perpetual group by datestamp ORDER BY datestamp DESC;
TIMESCALE_PWD = "password"
# TABLE_NAME = "bitstamp_1h"
TABLE_NAME = "bitmex_perpetual"
DATE_FIELD = "Date"

import sqlalchemy
import pandas as pd

# df = pd.read_csv("DATASET.CSV", parse_dates=["Date"])
# df = pd.read_csv(".\data\Bitstamp_BTCUSD_d.csv", parse_dates=["Date"])
# df = pd.read_csv(".\data\Bitstamp_BTCUSD_1h.csv", parse_dates=[DATE_FIELD])
print ("load csv")
df = pd.read_csv("/d1/code/python/backtrade/data/bitmex_btcusd-perpetual-futures_1min.csv", parse_dates=[DATE_FIELD])
print (df)

engine = sqlalchemy.create_engine(f"postgresql://postgres:{TIMESCALE_PWD}@localhost/trading")
conn = engine.connect()
df.to_sql(TABLE_NAME, con=conn, if_exists="replace") # append

res = conn.execute(f"SELECT create_hypertable('{TABLE_NAME}', '{DATE_FIELD}', migrate_data => true)")
print(res)
