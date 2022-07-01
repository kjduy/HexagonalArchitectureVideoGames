from fastapi import FastAPI

from .videogame.videogame_container import VideogameContainer
from .user.user_container import UserContainer
from .level.level_container import LevelContainer
from .videogame import router as videogame_router
from .user import router as user_router
from .level import router as level_router

app = FastAPI()

videogame_container = VideogameContainer()
videogame_container.wire(modules=[videogame_router])
app.container = videogame_container

user_container = UserContainer()
user_container.wire(modules=[user_router])
app.container = user_container

level_container = LevelContainer()
level_container.wire(modules=[level_router])
app.container = level_container

app.include_router(level_router.router)
