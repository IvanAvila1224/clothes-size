FROM python:3.8

# Actualiza el sistema e instala las bibliotecas necesarias
RUN apt-get update -y && \
    apt-get install -y libatlas-base-dev && \
    apt-get clean

WORKDIR /app
COPY ./requirements.txt ./requirements.txt
RUN pip install --no-cache-dir --upgrade -r ./requirements.txt
COPY ./app.py .
COPY ./model ./model
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]
