from os import getenv

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

USERNAME = getenv("POSTGRES_USERNAME", "postgres")
PASSWORD = getenv("POSTGRES_PASSWORD", "postgres")
DB = getenv("POSTGRES_DB", "fast_blog")
HOST = getenv("POSTGRES_HOST", "localhost")

DATABASE_URL = f"postgresql://{USERNAME}:{PASSWORD}@{HOST}/15489"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
