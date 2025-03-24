import pandas as pd
from sklearn.ensemble import IsolationForest

def detect_anomalies(data):
    """
    data is a list of numeric values
    """
    df = pd.DataFrame(data, columns=["value"])
    iso = IsolationForest(contamination=0.01, random_state=42)
    iso.fit(df)
    return iso.predict(df)