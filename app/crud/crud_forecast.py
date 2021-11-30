from typing import List
from sqlalchemy.orm import Session

from app.models import BeachForecastList


class CRUDForecast:
    def get_forecasts_by_beach_or_ocean(
        self, db: Session, *, beach: str, ocean: str
    ) -> List[BeachForecastList]:
        if beach and ocean:
            return (
                db.query(BeachForecastList)
                .filter(
                    BeachForecastList.beach.like(f"%{beach}%"),
                    BeachForecastList.ocean.like(f"{ocean}"),
                )
                .all()
            )
        elif beach and not ocean:
            return (
                db.query(BeachForecastList).filter(BeachForecastList.beach.like(f"%{beach}%")).all()
            )
        elif not beach and ocean:
            return (
                db.query(BeachForecastList).filter(BeachForecastList.ocean.like(f"{ocean}")).all()
            )
        return db.query(BeachForecastList).all()

    def get_forecast_detail(self, db: Session, beach_id: int) -> BeachForecastList:
        return db.query(BeachForecastList).filter(BeachForecastList.beach_id == beach_id).first()


forecast = CRUDForecast()
