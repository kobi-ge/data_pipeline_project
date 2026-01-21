import pandas as pd
import numpy as np
import requests
import os

URL = os.getenv("SERVER_C_URL", "http://localhost:8000")


def convert_to_df(data: list[dict]):
    df = pd.DataFrame(data)
    return df

def add_columns(df):
    temper_bins = [-np.inf, 18, 25, np.inf]
    temper_lab = ["cold", "moderate", "hot"]
    wind_bins = [0, 10, np.inf]
    wind_lab = ["calm", "windy"]
    df['temperature_category'] = pd.cut(df['temperature'], bins=temper_bins, labels=temper_lab)
    df['wind_status'] = pd.cut(df['wind_speed'], bins=wind_bins, labels=wind_lab)
    return df

def df_to_json(df: pd.DataFrame):
    json_df = df.to_json(orient="index")
    return json_df

def send_server_c(json_data):
    res = requests.post(url=URL, data=json_data)
    return res.json



