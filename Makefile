# Variables
VENV_BIN := .venv/bin
PYTHON := $(VENV_BIN)/python
DJANGO := $(PYTHON) manage.py

# === Django commands ===

run:
	$(DJANGO) runserver

migrate:
	$(DJANGO) migrate

makemigrations:
	$(DJANGO) makemigrations

shell:
	$(DJANGO) shell

createsuperuser:
	$(DJANGO) createsuperuser

check:
	$(DJANGO) check

test:
	$(DJANGO) test

collectstatic:
	$(DJANGO) collectstatic --noinput

# === Database ===

resetdb:
	rm -f db.sqlite3
	$(DJANGO) migrate

# === Clean ===

clean:
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete

.PHONY: run migrate makemigrations shell createsuperuser check test collectstatic resetdb clean
