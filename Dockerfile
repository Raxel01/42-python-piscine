FROM python:3.10-bullseye

WORKDIR 42-python-piscine

RUN pip install --upgrade pip

RUN  pip install flake8



copy . .