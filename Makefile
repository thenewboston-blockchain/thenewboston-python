.PHONY: build
build:
	poetry build -f sdist

.PHONY: install
install:
	poetry install

.PHONY: test
test:
	poetry run pytest --cov-config=.coveragerc --cov=./src

.PHONY: lint
lint:
	# TODO(dmu) MEDIUM: Consider moving tests into `src/thenewboston`
	poetry run flake8 src/thenewboston tests
