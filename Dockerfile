FROM python:3.11

WORKDIR /app

COPY scripts/ scripts/
RUN pip install pandas mysql-connector-python

CMD ["python", "scripts/extract.py"]