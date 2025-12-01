from fastapi import FastAPI
from app.api.v1_route_api import router as v1_router
from app.api.v2_route_api import router as v2_router

app = FastAPI(title="Notes API")

app.include_router(v1_router)
app.include_router(v2_router)

@app.get("/")
def root():
    return {"status": "running"}
