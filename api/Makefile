.PHONY: start start-dev stop stop-dev build build-dev logs logs-dev

start:
	docker-compose up -d

start-dev:
	docker-compose --file docker-compose.dev.yml up -d

stop:
	docker-compose down

stop-dev:
	docker-compose --file docker-compose.dev.yml down

build:
	docker-compose build

build-dev:
	docker-compose --file docker-compose.dev.yml build

logs:
	docker-compose logs -f

logs-dev:
	docker-compose --file docker-compose.dev.yml logs -f
