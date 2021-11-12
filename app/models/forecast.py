from sqlalchemy import Column, Integer, String, JSON
import sqlalchemy as sa
from sqlalchemy import Column
from sqlalchemy.dialects import postgresql

from app.db.base_class import Base


class BeachForecastList(Base):
    id = Column(Integer, primary_key=True, index=True)
    create_dt = Column(postgresql.TIMESTAMP(timezone=True), server_default=sa.func.now())
    update_dt = Column(
        postgresql.TIMESTAMP(timezone=True), default=sa.func.now(), onupdate=sa.func.now()
    )
    beach = Column(String, index=True)
    region = Column(String, index=True)
    ocean = Column(String, index=True)
    beach_id = Column(Integer, index=True)
    live_info = Column(JSON)
    forecast_info = Column(JSON)


class BeachForecastListHistory(Base):
    id = Column(Integer, primary_key=True, index=True)
    create_dt = Column(postgresql.TIMESTAMP(timezone=True), server_default=sa.func.now())
    update_dt = Column(
        postgresql.TIMESTAMP(timezone=True), default=sa.func.now(), onupdate=sa.func.now()
    )
    beach = Column(String, index=True)
    region = Column(String, index=True)
    ocean = Column(String, index=True)
    beach_id = Column(Integer, index=True)
    live_info = Column(JSON)
    forecast_info = Column(JSON)
