lint:
	poetry run flake8 --exclude .venv,*/migrations

build:
	./build.sh

run:
	poetry run python manage.py $(a)

dev:
	poetry run python manage.py runserver

mess:
	poetry run poetry run django-admin makemessages -a
	poetry run django-admin compilemessages

test:
	poetry run python manage.py test $(a)

.PHONY: coverage-run
coverage-run:
	poetry run coverage run manage.py test

.PHONY: coverage-run
coverage-xml: coverage-run
	coverage xml
