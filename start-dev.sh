#!/usr/bin/env bash
#alembic revision --autogenerate -m "update"

alembic upgrade head

gunicorn src.main:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000
