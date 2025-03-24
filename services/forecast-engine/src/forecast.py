import pandas as pd
from prophet import Prophet

def train_forecast_model(data):
    df = pd.DataFrame(data).rename(columns={"date": "ds", "revenue": "y"})
    model = Prophet(seasonality_mode="multiplicative")
    model.fit(df)
    return model

def create_forecast(model, days=30):
    future = model.make_future_dataframe(periods=days)
    forecast = model.predict(future)
    return forecast