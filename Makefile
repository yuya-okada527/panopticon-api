run:
	# docker-compose run web ./bin/start-local-env.sh
	docker-compose up -d --remove-orphans
migrate:
	docker-compose exec web rails db:create
	docker-compose exec web ridgepole -c config/database.yml -E development -f db/Schemafile --apply
	docker-compose exec web ridgepole -c config/database.yml -E test -f db/Schemafile --apply
down:
	docker-compose down
build:
	docker-compose build
update:
	docker-compose run web bundle
	docker-compose build
