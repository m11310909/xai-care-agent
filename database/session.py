from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///local.db", echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
