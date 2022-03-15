POETRY=poetry
UVICORN=$(POETRY) run uvicorn

install:
	$(POETRY) install
	$(POETRY_EXPORT)

run:
	${UVICORN} app_videogames.main:app --reload
