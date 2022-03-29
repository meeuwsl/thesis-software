.PHONY: main test cov install

main:
	python main.py

test:
	pytest tests/*

cov:
	pytest tests/* --cov

cov-fresh: install cov

install: 
	pip install -e .[dev]