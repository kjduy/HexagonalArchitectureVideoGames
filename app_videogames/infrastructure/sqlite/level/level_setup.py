from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

from ..videogame import VideogameTable, Base


class LevelTable(Base):

    __tablename__ = 'level'
    level_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    difficulty = Column(String, nullable=False)
    last_game_date = Column(String, nullable=True)
    videogame_id = Column(Integer,ForeignKey('videogame.videogame_id'))
    videogame = relationship(VideogameTable)


engine = create_engine('sqlite:///./db/app_videogames.db')
Base.metadata.create_all(engine)
