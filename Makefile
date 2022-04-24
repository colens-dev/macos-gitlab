setup:
	@echo "** Running python setup..."
	@echo "** Installing dependencies..."
	@pip install -r requirements.txt
	@echo "** Installing dev dependencies..."
	@pip install -r dev-requirements.txt

check:
	@echo "** Running lint and test check..."
	@flake8
	@pytest


flake8:
	@echo "** Running flake8..."
	@flake8

pytest:
	@echo "** Running python tests..."
	@pytest
