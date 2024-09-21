FROM postgres:16.4
ENV POSTGRES_PASSWORD=password
ENV POSTGRES_USER=user
ENV POSTGRES_DB=database
EXPOSE 5432
COPY create_fixtures.sql /docker-entrypoint-initdb.d/create_fixtures.sql
