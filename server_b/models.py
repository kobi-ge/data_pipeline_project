from pydantic import BaseModel, ValidationError,Field
import datetime

class LocationData(BaseModel):
    timestamp: str
    location_name: str
    country: str
    latitude: float
    longitude: float
    temperature: float
    wind_speed: float
    humidity: int


    
