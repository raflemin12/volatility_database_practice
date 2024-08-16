import pandas as pd
import os
from dotenv import load_dotenv
import psycopg2

vix_hist = pd.read_csv('https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv', index_col=False)

# change column names to lowercase

vix_hist.columns = [name.lower() for name in vix_hist.columns]

# change 'date' to datetime

vix_hist['date'] = pd.to_datetime(vix_hist['date'], yearfirst=True)

load_dotenv()

conn = psycopg2.connect(dbname=os.getenv("DBNAME"),
                        user=os.getenv("USER"),
                        password=os.getenv("PASSWORD"),
                        host=os.getenv("HOST"),
                        port=os.getenv("PORT"))

cur = conn.cursor()
