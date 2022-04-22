from fastapi import FastAPI

from app_videogames.api.videogame.videogame_container import VideogameContainer
from app_videogames.api.user.user_container import UserContainer
from app_videogames.api.videogame import router as videogame_router
from app_videogames.api.user import router as user_router

app = FastAPI()

videogame_container = VideogameContainer()
videogame_container.wire(modules=[videogame_router])
app.container = videogame_container

user_container= UserContainer()
user_container.wire(modules=[user_router])
app.container = user_container

app.include_router(videogame_router.router)
