run:
	# docker-compose run api ./bin/start-local-env.sh
	docker-compose up -d --remove-orphans
migrate:
	docker-compose exec api rails db:create
	docker-compose exec api ridgepole -c config/database.yml -E development -f db/Schemafile --apply
	docker-compose exec api ridgepole -c config/database.yml -E test -f db/Schemafile --apply
seed:
	docker-compose exec api rails db:seed
down:
	docker-compose down
build:
	docker-compose build
update:
	docker-compose run api bundle
	docker-compose build
