import models
import datetime
import pandas as pd

def validate_types(data: dict):
    try:
        valid_data = models.LocationData.model_validate(data)
        return valid_data
    except models.ValidationError as e:
        return f"invalid dict, error: {e}"
    

def convert_to_df(data: list[dict]):
    df = pd.DataFrame(data)
    return df

def add_columns(df):
    temper_bins = [0, 18, 25, 1000]
    temper_lab = ["cold", "moderate", "hot"]
    wind_bins = [0, 10, 1000]
    wind_lab = ["calm", "windy"]
    df['temperature_category'] = pd.cut(df['temperature'], bins=temper_bins, labels=temper_lab)
    df['wind_status'] = pd.cut(df['wind_speed'], bins=wind_bins, labels=wind_lab)
    return df





