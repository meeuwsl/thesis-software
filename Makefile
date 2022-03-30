.PHONY: main test cov install

main:
	python main.py

test:
	pytest main.py

cov:
	pytest main.py --cov

cov-fresh: install cov

install: 
	pip install -e .[dev]