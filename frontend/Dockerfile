FROM python:3.9

WORKDIR /app

ENV PYTHONUNBUFFERED 1

RUN pip --no-cache-dir install gunicorn virtualenv
RUN apt-get update && apt-get install -y build-essential python-dev

ADD . .

RUN virtualenv ./venv -p python3.9

RUN ./venv/bin/python3 -m pip install --upgrade pip

RUN ./venv/bin/pip3 install -r requirements.txt

EXPOSE 3000

ENTRYPOINT [ "./venv/bin/python3" ]

CMD ["run.py"]
