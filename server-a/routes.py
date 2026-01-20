from fastapi import APIRouter

router = APIRouter()

@router.post('/ingest')
def get_locations():
    return {'massage':'hi'}