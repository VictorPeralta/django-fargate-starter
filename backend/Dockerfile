# pull official base image
FROM python:3.11.1

# set work directory
WORKDIR /app

RUN apt update && apt install -y netcat

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# install poetry
ENV POETRY_HOME=/etc/poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH = "$PATH:$POETRY_HOME/bin"


# Install dependencies
COPY pyproject.toml . 
COPY poetry.lock .
RUN poetry config virtualenvs.create false
RUN poetry install


# Copy project
COPY . .


RUN ["chmod", "+x", "/app/launch.sh"]
# run launch.sh
CMD ["/app/launch.sh"]
