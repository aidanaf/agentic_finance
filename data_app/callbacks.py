import pandas as pd
from dash.dependencies import Input, Output
from fetch_data import fetch_data


def register_callbacks(app):
    @app.callback(
        [
            Output("stock-price-chart_OHLC", "figure"),
            Output("stock-price-chart_PR", "figure"),
            Output("stock-price-chart_MA", "figure"),
        ],
        [Input("refresh-button", "n_clicks")],
    )
    def update_graphs(n_clicks):
        df = fetch_data()

        # --------------------OHLC-------------------------------------
        figure_OHLC = {
            "data": [
                {
                    "x": df["timestep"],
                    "open": df["open"],
                    "high": df["high"],
                    "low": df["low"],
                    "close": df["close"],
                    "type": "candlestick",
                    "name": "OHLC",
                },
                {
                    "x": df.index,
                    "y": df["volume"],
                    "type": "bar",
                    "name": "Volume",
                    "yaxis": "y2",
                },
            ],
            "layout": {
                "title": f"{df['symbol'].iloc[0]} Stock OHLC and Volume",
                "plot_bgcolor": "black",
                "paper_bgcolor": "black",
                "font": {"family": "Arial", "color": "white"},
                "xaxis": {"showgrid": True, "gridcolor": "gray"},
                "yaxis": {"showgrid": True, "gridcolor": "gray"},
                "yaxis2": {"showgrid": True, "gridcolor": "gray"},
                "showlegend": False,
            },
        }

        # --------------------Price Ratio-------------------------------------
        figure_pr = {
            "data": [
                {
                    "x": df.index,
                    "y": df["price_ratio"],
                    "type": "line",
                    "name": "Price Ratio",
                }
            ],
            "layout": {
                "title": f"{df['symbol'].iloc[0]} Stock Price Ratio",
                "plot_bgcolor": "black",
                "paper_bgcolor": "black",
                "font": {"family": "Arial", "color": "white"},
                "xaxis": {"showgrid": True, "gridcolor": "gray"},
                "yaxis": {"showgrid": True, "gridcolor": "gray"},
                "showlegend": False,
            },
        }

        # --------------------Moving Average-------------------------------------
        figure_ma = {
            "data": [
                {
                    "x": df.index,
                    "y": df["moving_average"],
                    "type": "line",
                    "name": "Moving Average",
                }
            ],
            "layout": {
                "title": f"{df['symbol'].iloc[0]} Stock Moving Average",
                "plot_bgcolor": "black",
                "paper_bgcolor": "black",
                "font": {"family": "Arial", "color": "white"},
                "xaxis": {"showgrid": True, "gridcolor": "gray"},
                "yaxis": {"showgrid": True, "gridcolor": "gray"},
                "showlegend": False,
            },
        }

        return figure_OHLC, figure_pr, figure_ma
