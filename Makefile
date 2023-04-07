.DEFAULT_GOAL := install
.PHONY: install format lint mypy pyright checks safety

install: ## Install dependencies
	pip install -r requirements-dev.txt --upgrade --no-warn-script-location

format: ## Format
	python -m isort influxicate.py --skip .venv/
	python -m black influxicate.py --exclude .venv/

lint: ## Lint python files with flake8
	python -m flake8 influxicate.py

mypy: ## Check with mypy
	python -m mypy influxicate.py --ignore-missing-imports

pyright: ## Check with pyright
	python -m pyright influxicate.py

pylint: ## Check with pylint
	python -m pylint influxicate.py

checks: lint pylint mypy pyright test

safety: ## Check for dependencies security breach with safety
	python -m safety check
