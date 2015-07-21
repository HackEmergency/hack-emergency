FROM python:2.7
#RUN apt-get update
#RUN apt-get install python python-pip -y
# COPY requirements.txt .
# RUN mkdir /code
ADD . /code
ADD ../conf /etc/hackemergency
ADD ../celery_base /source/celery_base
WORKDIR /code
RUN ls > out.txt
RUN pip install -r requirements.txt
# CMD python app.py