FROM python:3.7.0

USER root

RUN mkdir -p /mlflow/

RUN chmod 777 -R /mlflow

WORKDIR /mlflow

RUN pip install mlflow==1.0.0
RUN pip install psycopg2

EXPOSE 5000

CMD mlflow server \
    --backend-store-uri $DB_URI \
    --default-artifact-root /mlflow \
    --host 0.0.0.0 \
    --port 5000 \
