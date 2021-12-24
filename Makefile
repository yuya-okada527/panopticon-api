run:
	docker-compose exec web ./bin/start-local-env.sh
down:
	docker-compose down
build:
	docker-compose build
