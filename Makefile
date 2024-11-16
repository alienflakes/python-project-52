lint:
	poetry run flake8 --exclude .venv --ignore=E501

run:
	poetry run python manage.py $(a)

dev:
	poetry run python manage.py runserver

mess:
	poetry run poetry run django-admin makemessages -a
	poetry run django-admin compilemessages

test:
	poetry run python manage.py test $(a)
