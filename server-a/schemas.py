from pydantic import BaseModel, Field

class LocationModel(BaseModel):
    location : str = Field(...,pattern=r"^[a-zA-Z\s]+$")