from sqlalchemy import create_engine, text
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "ETL")))

from fetch_data import reset_data
import config


def clear_dataframe():
    reset_data()
    print("Previously fetched data cleared.")


if __name__ == "__main__":
    user_input = (
        input("Do you want to clear all visualized data? (yes/no): ").strip().lower()
    )
    if user_input == "yes":
        clear_dataframe()
        print("Data cleared.")
    else:
        print("Data not cleared.")
