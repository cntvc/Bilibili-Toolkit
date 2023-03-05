all: lint test

tests=tests
src=bilibili_toolkit

test:
	poetry run pytest --cov=$(src) $(tests) --no-cov-on-fail --cov-report=html

lint:
	poetry run black $(src) $(tests)
	poetry run isort $(src) $(tests)
	poetry run flake8 $(src) $(tests)

clean:
	rm -rf htmlcov
	rm -rf .coverage
	rm -rf .pytest_cache
	rm -rf __pycache__
	rm -rf */__pycache__
	rm -rf */*/__pycache__
	rm -rf */*/*/__pycache__
