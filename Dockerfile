FROM python:latest

WORKDIR /app

ENV PYTHONPATH=/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN make format-check

ENTRYPOINT ["sh", "-c", "make test && make migrations && make run"]
