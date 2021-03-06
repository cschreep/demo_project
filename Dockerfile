FROM python:3.9-slim

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 5000

COPY . /app

RUN pip install .

CMD ["flask", "run", "--host=0.0.0.0"]
