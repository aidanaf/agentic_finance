import pandas as pd
import psycopg2
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import config

global_df = pd.DataFrame()


def fetch_data():
    global global_df
    conn = psycopg2.connect(
        dbname=config.DB_NAME,
        user=config.DB_USER,
        password=config.DB_PASSWORD,
        host=config.DB_HOST,
        port=config.DB_PORT,
    )
    global_df = pd.read_sql("SELECT * FROM stock_prices", conn)
    if "timestep" in global_df.columns:
        global_df.set_index("timestep", inplace=True)

    conn.close()
    return global_df


def reset_data():
    global global_df
    global_df = pd.DataFrame()
    conn = psycopg2.connect(
        dbname=config.DB_NAME,
        user=config.DB_USER,
        password=config.DB_PASSWORD,
        host=config.DB_HOST,
        port=config.DB_PORT,
    )
    cursor = conn.cursor()
    cursor.execute("DELETE FROM stock_prices")
    conn.commit()
    conn.close()
    print("Data reset in the database.")
