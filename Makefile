run:
	uvicorn src.app.main:app --reload
lint:
	poetry run pysen run lint
format:
	poetry run pysen run format
test:
	poetry run pytest src/tests -v --cov=src/app
watch:
	poetry run ptw src/tests
