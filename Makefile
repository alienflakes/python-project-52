lint:
	poetry run flake8 task_manager

dev:
	poetry run python manage.py runserver
