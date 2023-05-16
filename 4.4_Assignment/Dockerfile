FROM python:3.8-slim-buster

WORKDIR /home/app/

COPY ./ /home/app/

ENV debug=1

VOLUME /app/data

COPY requirements.txt .

RUN pip install -r requirements.txt

ENV PYTHONPATH=${PYTHONPATH}:/home/app/

CMD ["bash", "-c", "pip install -r requirements.txt && gunicorn main:app -b 0.0.0.0:5000"]
