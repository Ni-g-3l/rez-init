clean:
	find . -name \*.py[cod] -delete
	find . -name __pycache__ -delete

test:
	python -m unittest discover

coverage:
	coverage run -m unittest discover
	coverage report -m