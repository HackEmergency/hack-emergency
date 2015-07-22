FROM python:2.7
#RUN apt-get update
#RUN apt-get install python python-pip -y
# COPY requirements.txt .
# RUN mkdir /code
VOLUME /code
VOLUME /etc/hackemergency
ADD requirements.txt /code/requirements.txt
WORKDIR /code
RUN ls > out.txt
RUN pip install -r requirements.txt
# CMD python app.py