from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def create_session():
    engine = create_engine('sqlite:///./db/app_videogames.db')
    db_session = sessionmaker(bind=engine)
    session = db_session()
    return session
