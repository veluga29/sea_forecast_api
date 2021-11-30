from typing import Optional

from pydantic import BaseModel


# Base schema
class BeachForecastListBase(BaseModel):
    beach: Optional[str] = None
    region: Optional[str] = None
    ocean: Optional[str] = None
    beach_id: Optional[int] = None
    live_info: Optional[dict] = None
    forecast_info: Optional[dict] = None


# Schema with DB model 
class BeachForecastListInDBBase(BeachForecastListBase):
    id: int
    beach: str
    region: str
    ocean: str
    beach_id: int
    live_info: dict
    forecast_info: dict

    class Config:
        orm_mode = True


# Response model schema to client
class BeachForecastList(BeachForecastListInDBBase):
    pass

