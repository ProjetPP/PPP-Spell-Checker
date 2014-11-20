
PYTHON=python3

all: install

install:
	./dependencies.sh
	$(PYTHON) setup.py install

localinstall:
	./dependencies.sh
	$(PYTHON) setup.py install --user

run:
	gunicorn ppp_spell_checker:app

tests:
	$(PYTHON) run_tests.py

.PHONY: all install localinstall tests
