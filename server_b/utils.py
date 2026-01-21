import models
import datetime
import pandas as pd
import numpy as np
import json

def validate_types(data: dict):
    try:
        valid_data = models.LocationData.model_validate(data)
        return valid_data
    except models.ValidationError as e:
        return f"invalid dict, error: {e}"
    
def loop_validation(data: list[dict]):
    validated_list = []
    for val in data:
        validated_val = validate_types(val)
        print(type(validated_val))
        validated_dict = validated_val.model_dump(mode="json")
        validated_list.append(validated_dict)
    return validated_list

def convert_to_df(data: list[dict]):
    df = pd.DataFrame(data)
    return df

def add_columns(df):
    temper_bins = [0, 18, 25, np.inf]
    temper_lab = ["cold", "moderate", "hot"]
    wind_bins = [0, 10, np.inf]
    wind_lab = ["calm", "windy"]
    df['temperature_category'] = pd.cut(df['temperature'], bins=temper_bins, labels=temper_lab)
    df['wind_status'] = pd.cut(df['wind_speed'], bins=wind_bins, labels=wind_lab)
    return df

def df_to_json(df: pd.DataFrame):
    json_df = df.to_json(orient="index")
    return json_df



a = [{'timestamp': json.dumps(datetime.datetime(2026, 1, 19, 0, 0), default=str), 'location_name': 'Tel Aviv', 'country': 'Israel', 
      'latitude': 32.08088, 'longitude': 34.78057, 'temperature': 12.8, 'wind_speed': 3.1, 'humidity': 92}, 
      {'timestamp': datetime.datetime(2026, 1, 19, 1, 0), 'location_name': 'Tel Aviv', 'country': 'Israel', 
       'latitude': 32.08088, 'longitude': 34.78057, 'temperature': 12.8, 'wind_speed': 4.1, 'humidity': 90}]

b = {'timestamp': datetime.datetime(2026, 1, 19, 1, 0), 'location_name': 'Tel Aviv', 'country': 'Israel', 
       'latitude': 32.08088, 'longitude': 34.78057, 'temperature': 12.8, 'wind_speed': 4.1, 'humidity': 90}

#print(loop_validation(a))
#print(type(validate_types(b)))

c = convert_to_df(a)
print(df_to_json(c))