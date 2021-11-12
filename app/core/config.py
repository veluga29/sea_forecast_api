import os


API_V1_STR: str = "/api/v1"

POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "")
POSTGRES_USER: str = os.getenv("POSTGRES_USER", "")
POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", "")
POSTGRES_DB: str = os.getenv("POSTGRES_DB", "")
POSTGRES_PORT: str = os.getenv("POSTGRES_PORT", "")

PROJECT_NAME = os.getenv("PROJECT_NAME")

SQLALCHEMY_DATABASE_URI = "postgresql://{}:{}@{}:{}/{}".format(
    POSTGRES_USER,
    POSTGRES_PASSWORD,
    POSTGRES_SERVER,
    POSTGRES_PORT,
    POSTGRES_DB
)
