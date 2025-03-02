# Command
ISORT = isort .
BLACK = black .
FORMAT = ruff check .
ALEMBIC = alembic
START = uvicorn
DOCKER = docker-compose
PYTEST = pytest

# Target
TARGET = src.main:app
TEST_DIR = tests/

# Flags
ALEMBIC_FLAGS = revision --autogenerate -m "Welcom to docker"
UPG_FLAGS = upgrade head
UV_FLAGS = --host 0.0.0.0 --port 8000 --reload
DOCKER_FL = up --build
PYTEST_FL = -v -s $(TEST_DIR) --disable-warnings

dc:
	$(ISORT) && $(BLACK) && $(FORMAT) --fix
	$(DOCKER) $(DOCKER_FL)

format-check:
	$(FORMAT)

format:
	$(ISORT) && $(BLACK) && $(FORMAT) --fix

migrations:
	echo "⏳ Waiting for Postgres is ready..."
	sleep 5
	$(ALEMBIC) $(ALEMBIC_FLAGS)
	$(ALEMBIC) $(UPG_FLAGS) 

test:
	echo "🔨 Testing API..."
	sleep 5
	$(PYTEST) $(PYTEST_FL)

run:
	$(START) $(TARGET) $(UV_FLAGS)

.PHONY: migrations run dc test
