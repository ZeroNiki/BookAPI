# Command
ISORT = isort .
BLACK = black .
FORMAT = ruff check .
ALEMBIC = alembic
START = uvicorn
DOCKER = docker-compose

# Target
TARGET = src.main:app

# Flags
ALEMBIC_FLAGS = revision --autogenerate -m "Welcom to docker"
UPG_FLAGS = upgrade head
UV_FLAGS = --host 0.0.0.0 --port 8000 --reload
DOCKER_FL = up --build

dc:
	$(ISORT) && $(BLACK) && $(FORMAT) --fix
	$(DOCKER) $(DOCKER_FL)

format-check:
	$(FORMAT)

format:
	$(ISORT) && $(BLACK) && $(FORMAT) --fix

migrations:
	echo "⏳ Ждём, пока Postgres будет готов..."
	sleep 5
	$(ALEMBIC) $(ALEMBIC_FLAGS)
	$(ALEMBIC) $(UPG_FLAGS) 

run:
	$(START) $(TARGET) $(UV_FLAGS)

.PHONY: migrations run dc
