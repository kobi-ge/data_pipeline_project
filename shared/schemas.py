from pydantic import BaseModel, Field
from datetime import datetime


class LocationModel(BaseModel):
    location : str = Field(...,pattern=r"^[a-zA-Z\s]+$")

class LocationData(BaseModel):
    timestamp: datetime
    location_name: str
    country: str
    latitude: float
    longitude: float
    temperature: float
    wind_speed: float
    humidity: int

class LstLocation(BaseModel):
    location_info : list[LocationData] 