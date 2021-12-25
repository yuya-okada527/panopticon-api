run:
	# docker-compose run web ./bin/start-local-env.sh
	docker-compose up -d --remove-orphans
down:
	docker-compose down
build:
	docker-compose build
update:
	docker-compose run web bundle
	docker-compose build
