clean:
	@echo "-------------------- CLEAN PACKAGE -------------------- "
	find . -name \*.pyc -delete
	find . -name __pycache__ -delete
	@echo "------------------------------------------------------- "

test:
	@echo "---------------------- RUN TESTS ---------------------- "
	python3 -m unittest discover tests
	@echo "------------------------------------------------------- "
