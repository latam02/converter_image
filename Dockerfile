FROM python:3.8-slim

# This prevents Python from writing out pyc files
ENV PYTHONDONTWRITEBYTECODE 1

# This keeps Python from buffering stdin/stdout
ENV PYTHONUNBUFFERED 1

WORKDIR /src

COPY ./requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

RUN apt update && apt install imagemagick -y

# Install application into container
COPY . .

EXPOSE 8000

# ENTRYPOINT ["python","./manage.py","runserver"]
ENTRYPOINT ["echo","/dev/null"]