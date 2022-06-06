POETRY=poetry
PYTEST=$(POETRY) run pytest
UVICORN=$(POETRY) run uvicorn
PYLINT=$(POETRY) run pylint
PACKAGE=app_videogames

install:
	$(POETRY) install
	$(POETRY_EXPORT)

test:
	$(PYTEST) -vv

run:
	${UVICORN} ${PACKAGE}.infrastructure.api.main:app --reload

lint:
	$(PYLINT) ${PACKAGE}
