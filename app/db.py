from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

POSTGRES_URL = "postgresql://postgres:postgres@localhost:5432/postgres"

engine = create_engine(POSTGRES_URL, echo=False, pool_size=5, max_overflow=0)
DBSession = sessionmaker(bind=engine)
session = DBSession()