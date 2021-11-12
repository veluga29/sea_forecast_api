from fastapi import FastAPI

from app.api.api_v1.api import api_router
from app.core import config as settings

app = FastAPI(
    title=settings.PROJECT_NAME, redoc_url='/redoc', openapi_url=f"/core{settings.API_V1_STR}/openapi.json"
)

app.include_router(api_router, prefix=settings.API_V1_STR)