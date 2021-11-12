from typing import Optional

from pydantic import BaseModel


# Shared properties
class BeachForecastListBase(BaseModel):
    beach: Optional[str] = None
    region: Optional[str] = None
    ocean: Optional[str] = None


# Properties to receive on BeachForecastList creation
class BeachForecastListCreate(BeachForecastListBase):
    beach: str
    region: str
    ocean: str
    live_info: dict
    forecast_info: dict


# Properties to receive on BeachForecastList update
class BeachForecastListUpdate(BeachForecastListBase):
    beach: str
    region: str
    ocean: str
    live_info: dict
    forecast_info: dict


# Properties shared by models stored in DB
class BeachForecastListInDBBase(BeachForecastListBase):
    id: int
    beach: str
    region: str
    ocean: str
    live_info: dict
    forecast_info: dict

    class Config:
        orm_mode = True


# Properties to return to client
class BeachForecastList(BeachForecastListInDBBase):
    pass


# Properties properties stored in DB
class BeachForecastListInDB(BeachForecastListInDBBase):
    pass
