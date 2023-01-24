FROM python:3.10-slim
WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 8000
COPY . .

ENTRYPOINT ["bash", "entrypoint.sh"]
CMD python manage.py runserver 0.0.0.0:8000
