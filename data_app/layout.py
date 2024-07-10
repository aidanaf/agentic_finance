from dash import dcc, html
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from fetch_data import fetch_data

df = fetch_data()
stock_symbol = df["symbol"].unique()[0]  # Assuming there is at least one symbol

# --------------------OHLC-------------------------------------------------
fig_OHLC = make_subplots(
    rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.02, row_width=[0.2, 0.7]
)

fig_OHLC.add_trace(
    go.Candlestick(
        x=df.index,
        open=df["open"],
        high=df["high"],
        low=df["low"],
        close=df["close"],
        name="Candlestick",
    ),
    row=1,
    col=1,
)

fig_OHLC.add_trace(
    go.Bar(x=df.index, y=df["volume"], name="Volume", marker_color="red"),
    row=2,
    col=1,
)

fig_OHLC.update_layout(
    title=f"{stock_symbol} Stock OHLC and Volume",
    plot_bgcolor="black",
    paper_bgcolor="black",
    font=dict(family="Arial", color="white"),
    xaxis=dict(showgrid=True, gridcolor="gray"),
    yaxis=dict(showgrid=True, gridcolor="gray"),
    yaxis2=dict(showgrid=True, gridcolor="gray"),
    showlegend=False,
)

# --------------------Price Ratio-------------------------------------
fig_pr = px.line(df, x=df.index, y=df.price_ratio, title="Price Ratio")
fig_pr.update_layout(
    title=f"{stock_symbol} Stock Price Ratio",
    plot_bgcolor="black",
    paper_bgcolor="black",
    font=dict(family="Arial", color="white"),
    xaxis=dict(showgrid=True, gridcolor="gray"),
    yaxis=dict(showgrid=True, gridcolor="gray"),
    showlegend=False,
)

# --------------------Moving Average-------------------------------------
fig_ma = px.line(df, x=df.index, y=df.moving_average, title="Moving Average")
fig_ma.update_layout(
    title=f"{stock_symbol} Stock Moving Average",
    plot_bgcolor="black",
    paper_bgcolor="black",
    font=dict(family="Arial", color="white"),
    xaxis=dict(showgrid=True, gridcolor="gray"),
    yaxis=dict(showgrid=True, gridcolor="gray"),
    showlegend=False,
)

# --------------------Layout-------------------------------------------------
layout = html.Div(
    style={"backgroundColor": "black", "color": "white"},
    children=[
        html.H1(
            children="Stock Data Visualization",
            style={"textAlign": "left", "color": "white", "fontFamily": "Arial"},
        ),
        dcc.Graph(id="stock-price-chart_OHLC", figure=fig_OHLC),
        dcc.Graph(id="stock-price-chart_PR", figure=fig_pr),
        dcc.Graph(id="stock-price-chart_MA", figure=fig_ma),
        html.Button("Refresh Data", id="refresh-button", n_clicks=0),
    ],
)
