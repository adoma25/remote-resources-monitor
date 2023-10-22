FROM python:3.8

ADD main.py .

RUN pip install fabric

CMD ["python", "./main.py"]