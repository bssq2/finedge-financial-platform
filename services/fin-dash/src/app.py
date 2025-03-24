import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

def fetch_data():
    # In real scenarios, call a microservice or DB to get financial data
    data = [
        {"month": "2023-01", "revenue": 10000},
        {"month": "2023-02", "revenue": 15000},
        {"month": "2023-03", "revenue": 18000},
    ]
    return pd.DataFrame(data)

df = fetch_data()
fig = px.line(df, x="month", y="revenue", title="Monthly Revenue Trend")

app.layout = html.Div([
    html.H1("FinEdge Dashboard"),
    dcc.Graph(figure=fig)
])

server = app.server

if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=8050, debug=True)