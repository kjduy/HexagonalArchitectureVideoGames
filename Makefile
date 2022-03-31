POETRY=poetry
UVICORN=$(POETRY) run uvicorn

install:
	$(POETRY) install
	$(POETRY_EXPORT)

run:
	${UVICORN} app_videogames.api.main:app --reload
