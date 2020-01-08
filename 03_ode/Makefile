.PHONY: test clean

test:
	coverage run --source=. -m unittest ode.py && coverage html

clean:
	rm -rf *~ *.pyc __pycache__ htmlcov .coverage
