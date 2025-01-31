from fastapi import FastAPI
from workout_api.routers import api_router

app = FastAPI(title="Workout API", version="0.1.0")
app.include_router(api_router)