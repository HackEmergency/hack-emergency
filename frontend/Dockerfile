FROM python:2.7
#RUN apt-get update
#RUN apt-get install python python-pip -y
# COPY requirements.txt .
VOLUME /code
WORKDIR /code
ADD requirements.txt /code/requirements.txt
RUN ls > out.txt
RUN pip install -r requirements.txt
#This copies it for deployment
# ADD app.py /code/app.py
ADD . .
# EXPOSE 5000
CMD python app.py
# CMD /bin/bash