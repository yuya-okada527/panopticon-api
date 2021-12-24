#!bin/sh -veu
docker-compose up -d --remove-orphans
docker-compose exec web rails db:creat
