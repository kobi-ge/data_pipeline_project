from fastapi import APIRouter,Depends
from ..db.mysql_db import db_manager
from mysql.connector.abstracts import MySQLConnectionAbstract # הייבוא לטובת הטיפוס
from shared.schemas import LstLocationForDB, LocationForDB
import os 


TABLE_NAME = os.getenv("TABLE_NAME", "records_table")
DATABASE_NAME = os.getenv("DATABASE_NAME","sql_db")
router = APIRouter()

@router.post('/records')
def save_records(database : MySQLConnectionAbstract = Depends(db_manager.get_db)):
    cursor = database.cursor(dictionary=True)
    columns = ['timestamp','location_name','country','latitude','longitude','temoerature','wind_speed','humidity','temperature_category','wind_category']
    flags = '%s' * len(columns)
    cursor.execute(
        f"""INSERT INTO {TABLE_NAME} ({','.join(columns)}) VALUES ({flags}),
        """)