import extract
import transform
import load
import sys
from datetime import datetime


"""
def clear_table(table_name):
    conn = psycopg2.connect(
        database="your_db",
        user="your_user",
        password="your_password",
        host="your_host",
        port="your_port",
    )
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM {table_name};")
    conn.commit()
    cursor.close()
    conn.close()
"""


def log_message(message):
    with open("log.txt", "a") as log_file:
        log_file.write(f"{datetime.now()} - {message}\n")


def pipeline(stock_symbol, start_date, end_date):

    # extract
    try:
        data = extract.extract_stock_data(stock_symbol, start_date, end_date)
        print("extraction successful:", data)
        log_message("extraction successful")
    except Exception as e:
        print("extract failed", e)
        log_message("extraction failed")
        return

    # transform
    try:
        transformed_data = transform.transform(data, stock_symbol)
        print(transformed_data)
        log_message("transformation successful")
    except Exception as e:
        print("transform failed", e)
        log_message("transformation failed")
        return

    # load
    try:
        load.load_data_to_db(transformed_data, table_name)
        print("loading successful")
        log_message("loading successful")
    except Exception as e:
        print("loading failed", e)
        log_message("loading failed")


if __name__ == "__main__":
    table_name = "stock_prices"
    if len(sys.argv) != 4:
        print("Usage: main.py <stock_symbol> <start_date> <end_date>")
        sys.exit(1)

    stock_symbol = sys.argv[1]
    start_date = sys.argv[2]
    end_date = sys.argv[3]

    pipeline(stock_symbol, start_date, end_date)

# to execute the pipeline, run ./execute_etl_pipeline.sh
