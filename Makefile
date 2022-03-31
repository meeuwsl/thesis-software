.PHONY: main test cov install

main:
	\
	source env/bin/activate \
	python main.py \

test:
	pytest main.py

cov:
	pytest main.py --cov

cov-fresh: install cov

install: 
	pip install -e .[dev]

