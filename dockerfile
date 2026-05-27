FROM python:3.12.5

WORKDIR /main

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8000

CMD python3 manage.py runserver

