FROM python:3.11.4-slim

COPY requirements.txt .
RUN pip install --user -r requirements.txt

ENV PYTHONUNBUFFERED 1

WORKDIR /opt/trip-planner
COPY . .

ENTRYPOINT ["python3"]
CMD ["manage.py", "runserver", "0.0.0.0:8000"]