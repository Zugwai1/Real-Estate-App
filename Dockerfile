FROM python:3.10
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
RUN python3 manage.py migrate
CMD ["python3", "manage.py", "runserver"]