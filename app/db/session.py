import os
from sqlmodel import create_engine, Session
from app.config import settings

engine = create_engine(settings.get("DATABASE_URL"), echo=True)
print("ENV:", os.environ.get("DATABASE_URL"))  # Also check .env load
print("From Dynaconf:", settings.to_dict())

def get_session():
    with Session(engine) as session:
        yield session
