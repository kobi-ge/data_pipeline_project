from fastapi import APIRouter

router = APIRouter()

@router.get('/records')
def get_records():
    pass

@router.get('/records/count')
def get_count():
    pass

@router.get('/records/avg-temperature')
def get_avg():
    pass

@router.get('/records.max-wind')
def get_max():
    pass
@router.get('/records/extreme')
def get_extreme():
    pass
