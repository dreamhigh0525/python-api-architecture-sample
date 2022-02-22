## multi stage build
FROM python:3.10 as builder
WORKDIR /usr/src/app
RUN pip install poetry
COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false
RUN poetry export -f requirements.txt > requirements.txt


FROM python:3.10
ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/app
COPY --from=builder /usr/src/app/requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD [ "uvicorn", "src.inference.app:api", "--host", "0.0.0.0" ]
