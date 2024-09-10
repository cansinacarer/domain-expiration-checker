FROM python:3.11-slim

ADD . /app

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY run.py .

ENV PYTHONUNBUFFERED=1

CMD ["python", "run.py"]
