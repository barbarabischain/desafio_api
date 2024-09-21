FROM python:3.8
WORKDIR /app
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY pokemon.py pokemon.py
CMD ["python", "-u", "pokemon.py"]
