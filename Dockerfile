FROM python:3.10-alpine

ENV PYTHONBUFFERED 1

# home directory with app
WORKDIR /app

# update pip before install dependensies
RUN apk update && apk upgrade
RUN apk install -y apt-utils build-essential gcc swig libmariadb-dev-compat libmariadb-dev libpangocairo-1.0-0 ruby-full
RUN pip install -U pip
RUN pip install flake8==3.9.2
RUN flake8 --ignore=E501,F401 .

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
