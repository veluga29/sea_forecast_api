import os


PROJECT_NAME: str = os.getenv("PROJECT_NAME")
API_V1_STR: str = "/api/v1"

DB_HOST: str = os.getenv("DB_HOST", "")
DB_USER_NAME: str = os.getenv("DB_USER_NAME", "")
DB_USER_PASSWORD: str = os.getenv("DB_USER_PASSWORD", "")
DB_NAME: str = os.getenv("DB_NAME", "")
DB_PORT: str = os.getenv("DB_PORT", "")


DATABASE_URL = (
    f'postgresql://{DB_USER_NAME}:{DB_USER_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
)
