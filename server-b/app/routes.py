from fastapi import APIRouter
from .utils import *
from shared.schemas import LstLocation
router = APIRouter()
    
@router.post("/clean")
def clean_send(data: LstLocation):
    data_as_dicts = [item.model_dump() for item in data.location_info]
    df = convert_to_df(data_as_dicts)
    complete_df = add_columns(df)
    data_df_pydantic = df_to_dict(complete_df)
    response = send_server_c(data_df_pydantic)
    return response

