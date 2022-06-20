FROM python:3.9-slim-buster

WORKDIR /usr/app/src

RUN pip install --upgrade pip
RUN pip install flask
RUN pip install flask-cors
RUN pip install flask-socketio

EXPOSE 80

CMD ["python", "-u", "server.py"]