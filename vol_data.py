import os
from io import StringIO
import pandas as pd
from dotenv import load_dotenv
import psycopg2

vix_hist = pd.read_csv('https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv',
                       index_col=False)

# change column names to lowercase

vix_hist.columns = [name.lower() for name in vix_hist.columns]

# change 'date' to datetime

vix_hist['date'] = pd.to_datetime(vix_hist['date'], yearfirst=True)

load_dotenv(override=True)

conn = psycopg2.connect(dbname=os.getenv("DBNAME"),
                        user=os.getenv("USER"),
                        password=os.getenv("PASSWORD"),
                        host=os.getenv("HOST"),
                        port=os.getenv("PORT")
)

conn.autocommit = True
cur = conn.cursor()

cur.execute("CREATE DATABASE volatility;")

cur.close()
conn.close()

conn_v = psycopg2.connect(dbname='volatility',
                        user=os.getenv("USER"),
                        password=os.getenv("PASSWORD"),
                        host=os.getenv("HOST"),
                        port=os.getenv("PORT")
)

conn_v.autocommit = True
cur_v = conn_v.cursor()

cur_v.execute("CREATE TABLE vix("
             "vix_id SERIAL PRIMARY KEY,"
             "date DATE,"
             "open NUMERIC,"
             "high NUMERIC,"
             "low NUMERIC,"
             "close NUMERIC);")

file = StringIO()

vix_hist.to_csv(file, index=False, header=False)

file.seek(0)

cur_v.copy_from(file,'vix', null='', sep=',', columns=('date', 'open', 'high', 'low', 'close'))

cur_v.execute("SELECT AVG(close) FROM vix;")
print(cur_v.fetchall())

cur_v.close()
conn_v.close()
