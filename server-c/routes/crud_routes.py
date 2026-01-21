from fastapi import APIRouter


router = APIRouter()

@router.post('/records')
def save_records():
    pass
