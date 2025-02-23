test:
	docker-compose run --rm web pytest
up: test
	docker-compose up --remove-orphans
