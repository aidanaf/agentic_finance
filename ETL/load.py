from sqlalchemy import create_engine
import config as config


def load_data_to_db(df, table_name):
    engine = create_engine(config.DATABASE_URI)
    df.to_sql(table_name, engine, if_exists="append", index=True)
