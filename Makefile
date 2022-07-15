.PHONY: main test cov install

main:
	source ./env/bin/activate \
	python main.py \

test:
	pytest -s main.py

cov:
	pytest -s main.py --cov

cov-fresh: install cov

install: 
	pip install -e .[dev]

