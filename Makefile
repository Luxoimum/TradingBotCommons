all: build test

build:
	@rm -rf dist
	@poetry build

format:
	@poetry run black .

lint:
	@poetry run pylint ./src ./handlers
	@poetry run black --check .

test:
	@poetry run pytest --cov=./src

watch:
	@poetry run ptw

install:
	@poetry lock
	@poetry install

version:
	@git add pyproject.toml
	@git commit -m "$$(poetry version -s)"
	@git tag --sign "v$$(poetry version -s)" -m "$(poetry version -s)"
	@git push --follow-tags

.PHONY: build format lint test watch version
