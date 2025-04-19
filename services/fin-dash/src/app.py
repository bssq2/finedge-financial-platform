import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)
server = app.server

def fetch_data():
    # In a real scenario, fetch from microservices or DB
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