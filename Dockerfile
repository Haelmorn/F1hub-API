FROM python:3

WORKDIR /f1hub

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . /f1hub

EXPOSE $PORT

CMD gunicorn --bind 0.0.0.0:$PORT f1hub.f1hub.wsgi:application
