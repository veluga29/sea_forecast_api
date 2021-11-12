from typing import Any, Optional, List

from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps


router = APIRouter()


@router.get("/beach", response_model=List[schemas.BeachForecastList])
def read_beach_forecast_list(
    db: Session = Depends(deps.get_db), beach: Optional[str] = None, ocean: Optional[str] = None
) -> Any:
    """
    Retrieve beach list and livecast information of each beach.
    """
    try:
        # read data by beach or ocean
        return crud.forecast.get_multi_by_beach_or_ocean(db, beach=beach, ocean=ocean)
    except Exception as e:
        raise HTTPException(status_code=404, detail="Item not found")


@router.get("/beach/{beach_id}", response_model=schemas.BeachForecastList)
def read_beach_forecast_detail(*, db: Session = Depends(deps.get_db), beach_id: int):
    """
    Retrieve beach list and livecast information of each beach.
    """
    try:
        return crud.forecast.get_forecast_detail(db, beach_id=beach_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail="Item not found")
