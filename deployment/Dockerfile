# docker build -t clean_architecture .
# docker run --rm -d --name=rest_graphql --env ENVIRONMENT=dev --env DB_DIALECT=postgresql --env DB_USER=postgres --env DB_PASSWORD=postgres --env DB_HOST=localhost --env DB_PORT=5432 --env DB_NAME=clean_architecture_db -p 5555:5000 clean_architecture

FROM python:alpine3.16

LABEL maintainer='Jorge Cardona <https://github.com/JorgeCardona>'

RUN pip3 -q install pip --upgrade


COPY ../requirements/requirements.txt ./tmp/requirements.txt
RUN apk update
RUN apk add postgresql-dev gcc python3-dev musl-dev

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql \
    && apk add postgresql-dev \
    && apk del build-deps
	
RUN pip install --no-cache-dir -r /tmp/requirements.txt


COPY ../application /application

WORKDIR /application
ENV ENVIRONMENT=dev
ENV DB_DIALECT=postgresql
ENV DB_USER=postgres
ENV DB_PASSWORD=postgres
ENV DB_HOST=localhost
ENV DB_PORT=5432
ENV DB_NAME=clean_architecture_db

# comandos para iniciar la aplicacion en http://localhost:5000
CMD ["uvicorn", "main:clean_architecture", "--host", "0.0.0.0", "--port", "5000"]

