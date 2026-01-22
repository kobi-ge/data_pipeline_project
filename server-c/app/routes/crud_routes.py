from fastapi import APIRouter,Depends
from ..db.mysql_db import db_manager
from mysql.connector.abstracts import MySQLConnectionAbstract # הייבוא לטובת הטיפוס
from shared.schemas import LstLocationForDB, LocationForDB
import os 


TABLE_NAME = os.getenv("TABLE_NAME", "records_table")
DATABASE_NAME = os.getenv("DATABASE_NAME","sql_db")
router = APIRouter()

@router.post('/records')
def save_records(payload: LstLocationForDB, database : MySQLConnectionAbstract = Depends(db_manager.get_db)):
    data = payload.locations_info
    fields = list(LocationForDB.model_fields.keys())
    values = [
        tuple(item.model_dump().values()) 
        for item in data
    ]
    try:
        cursor = database.cursor(dictionary=True)
        columns = ','.join(fields)
        flags = ','.join(['%s'] * len(fields))
        cursor.execute(f"USE {DATABASE_NAME}")

        query = f"INSERT INTO {TABLE_NAME} ({columns}) VALUES ({flags})"
        cursor.executemany(query,values)
        rows_inserted = cursor.rowcount
        database.commit()
            
        return {
            "status": "success",
            "message": f"Successfully inserted {rows_inserted} records",
            "count": rows_inserted
        }
    except Exception as e:
        
        database.rollback()
        return {
            "status": "error",
            "message": f"Failed to save records: {str(e)}"
        }
    finally:
        cursor.close()
