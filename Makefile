run:
	python manage.py runserver --settings=settings.local

migrate:
	python manage.py migrate --settings=settings.local

makemigrations:
	python manage.py makemigrations --settings=settings.local

run-prod:
	python manage.py runserver --settings=settings.prod