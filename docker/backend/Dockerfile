FROM python:3.8.5

WORKDIR /usr/app/

RUN pip install --upgrade pip
RUN pip install flask
RUN pip install flask-cors
RUN pip install Flask-Migrate
RUN pip install flask_sqlalchemy 
RUN pip install psycopg2-binary
RUN pip install flask_healthz

EXPOSE 80

CMD ["python", "-u", "app.py"]