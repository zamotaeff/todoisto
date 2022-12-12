FROM python:3.10-alpine

# create directory for the app user
RUN mkdir -p /app

# create the app user
RUN addgroup -S app && adduser -S app -G app

# home directory with app
ENV HOME /app
WORKDIR $HOME

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && apk upgrade
# update pip before install dependensies
RUN pip install -U pip
RUN pip install flake8==3.9.2
RUN flake8 --ignore=E501,F401 .

# install dependensies by poetry
COPY poetry.lock .
COPY pyproject.toml .

# install dependensies by poetry
RUN pip install poetry==1.2.2
RUN poetry config virtualenvs.create false && poetry install

# copy entrypoint.prod.sh
COPY entrypoint.prod.sh .
RUN sed -i 's/\r$//g'  $HOME/entrypoint.prod.sh
RUN chmod +x  $HOME/entrypoint.prod.sh

# copy project
COPY . $HOME

# chown all the files to the app user
RUN chown -R app:app $HOME

# change to the app user
USER app

# entrypoint
ENTRYPOINT ["sh", "entrypoint.prod.sh"]
