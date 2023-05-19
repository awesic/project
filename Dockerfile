FROM python:3.11

RUN mkdir app

WORKDIR app
#RUN cd app

COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt
#RUN pip install -r requirements.txt

COPY . .

#WORKDIR app

RUN chmod a+x ./*.sh

#RUN alembic upgrade head

#RUN gunicorn src.main:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000