FROM python:3.10-alpine

ENV PYTHONBUFFERED 1

# home directory with app
WORKDIR /app

# update pip before install dependensies
RUN apk update && apk upgrade

RUN pip install -U pip

# install dependensies by poetry
RUN pip install poetry==1.2.2
COPY poetry.lock .
COPY pyproject.toml .
RUN poetry config virtualenvs.create false && poetry install

# copy project
COPY backend/ .

EXPOSE 8000

# entrypoint
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
