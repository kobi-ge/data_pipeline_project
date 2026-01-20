from fastapi import FastAPI, APIRouter

router = APIRouter()

@router.post("/clean")
def clean_send():
    pass
