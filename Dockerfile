FROM python:3

WORKDIR /app

COPY . .

RUN cd datos; pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH='.:../' 

ENV FLASK_APP=app.py

WORKDIR /app/datos

CMD ["/bin/bash", "-c",  "python app.py"]
