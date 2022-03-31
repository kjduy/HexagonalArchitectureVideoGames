from fastapi import FastAPI

from app_videogames.api.videogame import router
from app_videogames.api.videogame.videogame_container import VideogameContainer
from app_videogames.api.user.user_container import UserContainer


app = FastAPI()

container = VideogameContainer()
container.wire(modules=[router])
app.container = container

app.include_router(router.router)
