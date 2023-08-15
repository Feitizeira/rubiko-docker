FROM python:3.9

WORKDIR /app

COPY app.py .

RUN pip install Flask

ENV GREETINGS "Servidor en funcionamiento"

EXPOSE 5000

CMD ["python", "app.py"]