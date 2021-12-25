#!bin/sh -veu
docker-compose up -d --remove-orphans
docker-compose exec web rails db:create
docker-compose exec web ridgepole -c config/database.yml -E development -f db/Schemafile --apply
docker-compose exec web ridgepole -c config/database.yml -E test -f db/Schemafile --apply
