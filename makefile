.PHONY: lint format type-check test run

lint:
	ruff check . --fix

format:
	ruff format .

type-check:
	mypy .

test:
	pytest

code-quality:
	make lint
	make format
	make type-check
	make test

run:
	python -m app.main
