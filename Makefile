init:
	pip install -r requirements.txt

test:
	# nosetests tests
	python3 setup.py test
