#Python image
FROM python:3

#Prevents the container from hiding/buffering the output
ENV PYTHONUNBUFFERED 1

#Create, change to, and fill a directory with project files
RUN mkdir /code
WORKDIR /code
COPY . /code/

#Install requirements
RUN pip install -r requirements.txt