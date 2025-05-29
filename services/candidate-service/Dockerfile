from python:3.12-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

COPY ./services/candidate-service/requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY ./services/candidate-service .

RUN ["python", "manage.py", "migrate"]

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]

