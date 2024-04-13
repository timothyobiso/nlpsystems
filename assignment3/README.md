# Assignment 3
This code is run using Python 3.11. Necessary packages are proided in `requirements.txt.`

## Create Docker Images
To build the Docker image for the FastAPI REST app, run the following command:
```bash
$ docker build -t my-app-fastapi -f Dockerfile_fast .
```

To build the Docker image for the Flask app, run the following command:
```bash
$ docker build -t my-app-flask -f Dockerfile_flask .
```

To build the Docker image for the FastAPI REST app, run the following command:
```bash
$ docker build -t my-app-streamlit -f Dockerfile_streamlit .
```
## Running Docker Images
To run the Docker image for the FastAPI REST app, run the following command:
```bash
$ docker run -p 8000:8000 my-app-fastapi
```
Available [here](http://127.0.0.1:8000)


To run the Docker image for the Flask app, run the following command:
```bash
$ docker run -p 5000:5000 my-app-flask
```
Available [here](http://127.0.0.1:5000)

To run the Docker image for the Streamlit app, run the following command:
```bash
$ docker run -p 8501:8501 my-app-streamlit
```
Available [here](http://localhost:8501)

```bash
$ curl http://127.0.0.1:8000/
$ curl http://127.0.0.1:8000/ner -H "Content-Type: application/json" -d@input.json
$ curl http://127.0.0.1:8000/dep -H "Content-Type: application/json" -d@input.json
```
Both `/ner` and `/dep` accept a "pretty" parameter to format the data nicely:
```bash
$ curl http://127.0.0.1:8000/ner?pretty=true -H "Content-Type: application/json" -d@input.json
```