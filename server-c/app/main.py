from fastapi import FastAPI
from .routes.crud_routes import router as crud_router
from .routes.query_routes import router as query_router
from .db.mysql_db import db_manager
import uvicorn



app = FastAPI(title="server-c")

@app.on_event('startup')
def startup_event():
    print("Connecting to Database...")
    try:
        db_manager.initialize_pool()
        db_manager.init_database()
        db_manager.init_schema()
    except Exception as e:
        print(f'error from init table {e}')
    print("Database connected!")


app.include_router(crud_router)
app.include_router(query_router)

if __name__=='__main__':
    uvicorn.run(app,host='0.0.0.0',port=8002)