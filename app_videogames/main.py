from fastapi import FastAPI

from app_videogames.container import Container
from app_videogames.api import router

app = FastAPI()

container = Container()
container.wire(modules=[router])
app.container = container

app.include_router(router.router)
