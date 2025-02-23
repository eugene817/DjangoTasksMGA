test:
	docker-compose run --rm web pytest
up: test
	docker-compose run web python manage.py migrate
	docker-compose up --remove-orphans
