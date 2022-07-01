from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class SqliteRepository:

    session = None

    def __init__(self):
        engine = create_engine('sqlite:///./db/app_videogames.db')
        db_session = sessionmaker(bind=engine)
        self.session = db_session()


    @staticmethod
    def close_session(session):
        session.close()
