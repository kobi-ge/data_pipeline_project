from fastapi import FastAPI, APIRouter
import uvicorn

from routes import router


app = FastAPI()

app.include_router(router)


