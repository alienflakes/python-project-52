lint:
	poetry run flake8 .

dev:
	poetry run python manage.py runserver
