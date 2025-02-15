FROM python:3.12.3

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY receptsite .

CMD ["gunicorn", "receptsite.wsgi:application", "--bind", "0.0.0.0:8000"]