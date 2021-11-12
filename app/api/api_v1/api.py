from fastapi import APIRouter

from app.api.api_v1.endpoints import forecast

api_router = APIRouter()
api_router.include_router(forecast.router, prefix="/forecast", tags=["forecast"])