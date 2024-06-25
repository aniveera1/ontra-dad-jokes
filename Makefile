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
fmt:     ## Format code using black.
	black -l 100 .
