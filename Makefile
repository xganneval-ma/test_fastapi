init:
	docker-compose build

down:
	docker-compose down

run: down init
	docker-compose run --rm --service-ports app
