FROM python:3.9.12-alpine3.15

EXPOSE 5000

WORKDIR /app

COPY requrements.txt .

RUN pip install -r requrements.txt

COPY app.py .

CMD [ "python" , "app.py"]