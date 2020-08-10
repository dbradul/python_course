FROM python:3.7-alpine

RUN apk add --update

RUN mkdir /app
WORKDIR /app

COPY app.py /app
#COPY requirements.txt ./requirements.txt
#RUN pip install -r requirements.txt

CMD ["python", "app.py"]
