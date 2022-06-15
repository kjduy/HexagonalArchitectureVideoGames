from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

from app_videogames.infrastructure.sqlite.user import UserTable, Base


class VideogameTable(Base):

    __tablename__ = "videogame"
    idVideogame = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    price = Column(Float, nullable=False)
    description = Column(String, nullable=True)
    user_id = Column(Integer,ForeignKey("user.user_id"))
    user = relationship(UserTable)

engine = create_engine('sqlite:///./db/app_videogames.db')
Base.metadata.create_all(engine)
