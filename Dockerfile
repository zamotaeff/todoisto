FROM python:3.10-alpine

# home directory with app
WORKDIR /code

#ENV
COPY backend/.env.prod .env

# update pip before install dependensies
RUN apk update && apk upgrade
RUN pip install -U pip
RUN pip install flake8==3.9.2
RUN flake8 --ignore=E501,F401 .

# install dependensies by poetry
RUN pip install poetry==1.2.2
COPY backend/poetry.lock .
COPY backend/pyproject.toml .
RUN poetry config virtualenvs.create false && poetry install

# copy entrypoint.prod.sh
COPY backend/entrypoint.prod.sh .
RUN sed -i 's/\r$//g' entrypoint.prod.sh
RUN chmod +x entrypoint.prod.sh

# copy project
COPY . .

# entrypoint
ENTRYPOINT ["sh", "entrypoint.prod.sh"]