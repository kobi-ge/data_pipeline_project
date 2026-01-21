from fastapi import FastAPI, APIRouter
import models, utils

router = APIRouter()

@router.post("/clean")
def clean_send(data: list[dict]):
    validated_data = utils.loop_validation(data)
    df = utils.convert_to_df(validated_data)
    complete_df = utils.add_columns(df)
    json_df = utils.df_to_json(complete_df)
    return json_df
    
