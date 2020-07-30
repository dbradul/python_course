FROM python:3.8

RUN apt-get update

RUN mkdir /app
WORKDIR /app

COPY app.py /app
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

CMD ["python", "app.py"]

#FROM python:3.8
#
#RUN apt-get update && apt-get install -y --no-install-recommends \
#    python-dev \
#    python-setuptools
#
#RUN mkdir -p /app/src
#WORKDIR /app
#
#COPY requirements.txt ./requirements.txt
#RUN pip install -r requirements.txt
#
##COPY src/ ./src/
##COPY .flake8/ ./.flake8/
#
#WORKDIR /app/src
#
#ENV ENV_CONFIG app/settings/environment/dev.env
#
##EXPOSE 8010
#
#CMD ["python", "manage.py", "runserver", "0:8010", "--settings=app.settings.dev"]