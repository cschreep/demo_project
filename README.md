# Getting started

## Local env

1. Configure the environment

```shell script
cd demo_project
python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
pip install -e .
```

2. Run the webserver
```shell script
flask run
```

3. Access the service at `localhost:5000/?query=hello`

## Docker

1. Build the docker image
```shell script
docker build -t demo-project -f Dockerfile .
```

2. Run a docker container
```shell script
docker run --rm -p 5000:5000 demo-project
```

3. Access the service at `localhost:5000/?query=hello`
