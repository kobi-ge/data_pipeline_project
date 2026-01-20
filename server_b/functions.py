import models
import datetime

def validate_dict(data: dict):
    try:
        valid_data = models.LocationData.model_validate(data)
        return valid_data
    except models.ValidationError as e:
        return f"invalid dict, error: {e}"
    

