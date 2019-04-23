install:
	python setup.py install

install-dev:
	pip install -r requrements-dev.txt

clean:
	python setup.py clean
	@ rm -rf build dist russian_names.egg-info

lint: install-dev
	flake8 --ignore=E501 russian_names

test: install-dev
	pytest -v --cache-clear tests/*

wheel: clean install-dev lint test
	python setup.py bdist_wheel

.PHONY: install install-dev clean lint test wheel
