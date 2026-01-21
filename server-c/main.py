from fastapi import FastAPI
from routes.crud_routes import router as crud_router
from routes.query_routes import router as query_router
import uvicorn



app = FastAPI(title="server-c")

@app.on_event('startup')
def startup_event():
    print("Connecting to Database...")
    print("Database connected!")


app.include_router(crud_router)
app.include_router(query_router)

if __name__=='__main__':
    uvicorn.run(app,host='0.0.0.0',port=8000)