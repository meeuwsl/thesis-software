main:
	python main.py

test:
	pytest tests/*

cov:
	pytest tests/* --cov