.PHONY: help env install run lint

help:
	@echo "Available targets:"
	@echo "  env     - Set up virtual environment and .env file"
	@echo "  install - Install dependencies into the virtual environment"
	@echo "  run     - Run the CLI tool"
	@echo "  lint    - Run linting on the code"

env:
	uv venv && . .venv/bin/activate

install:
	uv pip install -e .[dev]

run:
	github-access

lint:
	ruff check src/
