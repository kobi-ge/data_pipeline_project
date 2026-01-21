from fastapi import APIRouter
from shared.schemas import LocationModel,LstLocation
from .data.ingestion_logic import ingest_weather_for_location
import os
import requests




SERVER_B_NAME = os.getenv('SERVER_B_NAME','localhost')
SERVER_B_PORT = os.getenv('SERVER_B_PORT','8001')
SERVER_B_TIMEOUT = int(os.getenv('SERVER_B_TIMEOUT','5'))

DESTANATION_URL = f"http://{SERVER_B_NAME}:{SERVER_B_PORT}"
router = APIRouter()

@router.post('/ingest')
def get_locations(location: LocationModel):
    location_info = LstLocation(location_info=ingest_weather_for_location(location))
    try:
        server_b_result = connecation_to_server_b(location_info)
    except requests.exceptions.Timeout:
        server_b_result = {"error": "Server B is taking too long to respond"}
    except requests.exceptions.ConnectionError:
        server_b_result = {"error": "Could not connect to Server B. Check Service name/DNS"}
    except requests.exceptions.HTTPError as err:
        server_b_result = {"error": f"Server B returned an error: {err.response.status_code}"}
    except Exception as exc:
        server_b_result = {"error": f"Unexpected error: {str(exc)}"}
    if not server_b_result.get('error'):
        server_b_result = 'done'
    return {'massage':server_b_result}

def connecation_to_server_b(data:LstLocation):
    data = data.model_dump(mode='json')
    res = requests.post(f"{DESTANATION_URL}/clean", json= data, timeout= SERVER_B_TIMEOUT)
    res.raise_for_status()
    return res.json()