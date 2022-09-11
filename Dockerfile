FROM python:3.10
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY . .
COPY wait_for_db.sh .
RUN pip install -r requirements.txt
RUN echo "Package Installation done"
CMD ["python3", "manage.py", "runserver","0.0.0.0:8000"]
