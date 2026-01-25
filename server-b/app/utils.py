import pandas as pd
import numpy as np
import requests
import os
from shared.schemas import LstLocationForDB

SERVER_C_NAME = os.getenv('SERVER_C_NAME',"localhost")
SERVER_C_PORT = int(os.getenv("SERVER_C_PORT","8002"))
SERVER_C_TIMEOUT = int(os.getenv("SERVER_C_TIMEOUT","5"))

DESTINATION_URL = f"http://{SERVER_C_NAME}:{SERVER_C_PORT}/records"

def convert_to_df(data: list[dict]):
    df = pd.DataFrame(data)
    return df

def add_columns(df):
    temper_bins = [-np.inf, 18, 25, np.inf]
    temper_lab = ["cold", "moderate", "hot"]
    wind_bins = [0, 10, np.inf]
    wind_lab = ["calm", "windy"]
    df['temperature_category'] = pd.cut(df['temperature'], bins=temper_bins, labels=temper_lab)
    df['wind_category'] = pd.cut(df['wind_speed'], bins=wind_bins, labels=wind_lab)
    return df

def df_to_json(df: pd.DataFrame):
    json_df = df.to_json(orient="index")
    return json_df

def df_to_dict(df:pd.DataFrame):
    data_dicts = df.to_dict(orient='records')
    locations = LstLocationForDB(locations_info=data_dicts)
    return locations

def send_server_c(data:LstLocationForDB):
    payload = data.model_dump(mode='json')
    res = requests.post(url= DESTINATION_URL, json= payload, timeout= SERVER_C_TIMEOUT)
    return res.json()



