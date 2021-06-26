FROM python:3.9-buster
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
ADD . /meeting_planner
WORKDIR /meeting_planner