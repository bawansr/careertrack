from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.core.config import settings


# Database configuration
connect_args = {}

if settings.database_url.startswith("sqlite"):
    connect_args = {"check_same_thread": False}


# Create database engine
engine = create_engine(
    settings.database_url,
    connect_args=connect_args
)


# Create session factory
SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False
)


# Database session dependency
def get_db() -> Generator[Session, None, None]:

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()