.PHONY: help
help:    ## Show the help.
	@echo "Usage: make <target>"
	@echo ""
	@echo "Targets:"
	@fgrep "##" Makefile | fgrep -v fgrep

.PHONY: install
install: ## Install project dependencies.
	pip install -r requirements.txt

.PHONY: fmt
fmt:     ## Format code using black and isort.
	black -l 100 .
	isort --profile black .

.PHONY: lint
lint:    ## Lint code using mypy.
	mypy src/
