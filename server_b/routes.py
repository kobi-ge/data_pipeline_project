from fastapi import FastAPI, APIRouter
import models, utils

router = APIRouter()
    
@router.post("/clean")
def clean_send(data: list[models.LocationData]):
    data_as_dicts = [item.model_dump() for item in data]
    df = utils.convert_to_df(data_as_dicts)
    complete_df = utils.add_columns(df)
    json_df = utils.df_to_json(complete_df)
    response = utils.send_server_c(json_df)
    return response

