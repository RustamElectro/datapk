FROM python:3.7-slim

RUN mkdir /datapk

COPY requirements.txt /datapk

RUN pip3 install -r /datapk/requirements.txt --no-cache-dir

COPY news/ /datapk

WORKDIR /datapk

CMD ["python3", "manage.py", "runserver", "0:8000"]