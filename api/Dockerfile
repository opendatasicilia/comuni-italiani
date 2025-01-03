FROM python:3.10-slim
WORKDIR /app

COPY pyproject.toml .
COPY src ./src
RUN pip install -e .

EXPOSE 8888
