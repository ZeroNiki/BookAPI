FROM python:latest

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN make format

ENTRYPOINT ["sh", "-c", "make migrations && make run"]
