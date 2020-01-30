from fastapi import FastAPI

from app import api

app = FastAPI(title='FastAPI Example', version='0.0.1')
app.include_router(api.v1.router)
