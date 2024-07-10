import pandas as pd


def transform(raw_data, symbol):

    if isinstance(raw_data, dict) and "values" in raw_data:
        values = raw_data["values"]
        print(f"values: {values}")

        df = pd.DataFrame(values)

        # ------------------------------------------------------------------------

        # standard transforms
        df["datetime"] = pd.to_datetime(df["datetime"])
        df["timestep"] = range(len(df["datetime"]))
        df.set_index("datetime", inplace=True)
        df = df.astype(float, errors="ignore")
        df["symbol"] = symbol

        # ------------------------------------------------------------------------

        # advanced transforms
        df["price_ratio"] = df["close"] / df["open"]
        df["moving_average"] = df["close"].rolling(window=5).mean()
        df["moving_average"].fillna(method="ffill", inplace=True)

        return df
    else:
        raise ValueError("raw_data is not in the expected format")
