.PHONY: test clean

test:
	coverage run --source=. -m unittest integrasjon.py && coverage html

clean:
	rm -rf *~ *.pyc __pycache__ htmlcov .coverage
