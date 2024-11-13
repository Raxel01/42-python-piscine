FROM python:3.10-bullseye

WORKDIR 42-python-piscine

RUN pip install --upgrade pip

RUN  pip install flake8

RUN pip install numpy

RUN pip install --upgrade build

# RUN python3 -m pip install --upgrade twine

copy . .