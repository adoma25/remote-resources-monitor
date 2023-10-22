FROM python:3.8

ADD main.py .

RUN pip install fabric
RUN pip install matplotlib

CMD ["python", "-u", "./main.py"]