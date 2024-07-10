import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import dash
from layout import layout
from callbacks import register_callbacks

app = dash.Dash(__name__)

server = app.server

app.layout = layout

register_callbacks(app)

if __name__ == "__main__":
    app.run_server(debug=True)
