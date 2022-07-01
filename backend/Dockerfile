FROM --platform=linux/amd64 tiangolo/uwsgi-nginx-flask:python3.8
COPY ./app /app

RUN apt-get update && \
    apt-get install -y apt-utils apt-transport-https
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/debian/8/prod.list > /etc/apt/sources.list.d/mssql-release.list

RUN apt-get update

RUN ACCEPT_EULA=Y apt-get install -y msodbcsql17 && \
    ACCEPT_EULA=Y apt-get install -y mssql-tools && \
    ACCEPT_EULA=Y apt-get install -y unixodbc-dev

RUN pip install --upgrade pip
RUN pip install flask
RUN pip install flask-cors
RUN pip install flask-socketio
RUN pip install Flask-Migrate
RUN pip install flask_sqlalchemy 
RUN pip install psycopg2-binary
RUN pip install pyodbc
RUN pip install uwsgi
