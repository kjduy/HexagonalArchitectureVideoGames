from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

from app_videogames.infrastructure.sqlite.videogame import VideogameTable, Base


class LevelTable(Base):

    __tablename__ = "level"
    idLevel = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    difficulty = Column(String, nullable=False)
    last_game_date = Column(String, nullable=True)
    idVideogame = Column(Integer,ForeignKey("videogame.idVideogame"))
    videogame = relationship(VideogameTable)

engine = create_engine('sqlite:///./db/app_videogames.db')
Base.metadata.create_all(engine)
