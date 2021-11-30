from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core import config as settings

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
