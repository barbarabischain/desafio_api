FROM postgres:12.20-alpine3.20
RUN apk add --no-cache python3 py3-pip py3-psycopg2 py3-requests
ENV POSTGRES_PASSWORD=password
ENV POSTGRES_USER=user
ENV POSTGRES_DB=database
COPY create_fixtures.sql /docker-entrypoint-initdb.d/create_fixtures.sql

RUN mkdir pasta
COPY pokemon.py /pasta/pokemon.py
