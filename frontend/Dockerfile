FROM python:2.7
#RUN apt-get update
#RUN apt-get install python python-pip -y
# COPY requirements.txt .
# RUN mkdir /code
ADD . /code
WORKDIR /code
RUN ls > out.txt
RUN pip install -r /code/requirements.txt
CMD python app.py