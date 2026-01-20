from pydantic import BaseModel, ValidationError
import datetime

class LocationData(BaseModel):
    timestamp: datetime.datetime
    location_name: str
    country: str
    latitude: float
    longitude: float
    temperature: float
    wind_speed: float
    humidity: int

