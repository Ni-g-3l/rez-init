clean:
	find . -name \*.py[cod] -delete
	find . -name __pycache__ -delete

install:
	rez python -m pip install .

uninstall:
	rez python -m pip uninstall rez_{{cookiecutter.extension_command}}

test:
	python -m unittest discover

coverage:
	coverage run -m unittest discover
	coverage report -m