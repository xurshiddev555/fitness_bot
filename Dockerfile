FROM python:3.12-slim

ENV PYTHONUNBUFFERED 1
ENV DATABASE_URL postgresql+psycopg2://postgres:1@localhost:5432/tg_users
ENV TELEGRAM_BOT_TOKEN 7457840472:AAHvkypMl62fEbAA5c-wk44pfEDc6a2yA4k
ENV SENDER_EMAIL sunatlohgafur1214@gmail.com
ENV EMAIL_PASSWORD rvztfwesraqpbszr

WORKDIR /app

COPY .. /app

RUN pip install --no-cache-dir -r /app/requirements.txt

CMD ["python", "./task_1_va_task_2.py"]
