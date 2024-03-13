# Assignment 1
This code is run using Python 3.11. Necessary packages are proided in `requirements.txt.`

## FastAPI
To run the FastAPI REST app, run the following command:
```bash
$ uvicorn app_fastapi:app --reload
```

Open another terminal window to interact with the REST API. The first command is a GET request. The others are POST requests.
The `input.json` file is provided in the repository.
```bash
$ curl http://127.0.0.1:8000/
$ curl http://127.0.0.1:8000/ner -H "Content-Type: application/json" -d@input.json
$ curl http://127.0.0.1:8000/dep -H "Content-Type: application/json" -d@input.json
```
Both `/ner` and `/dep` accept a "pretty" parameter to format the data nicely:
```bash
$ curl http://127.0.0.1:8000/ner?pretty=true -H "Content-Type: application/json" -d@input.json
```

## Flask
To run the Flask app, run the following command:
```bash
$ python app_flask.py
```
The Flask app will be available at [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## Streamlit
To run the Streamlit app, run the following command:
```bash
$ python -m streamlit run app_streamlit.py
```

The Streamlit app will be available at [http://localhost:8501/](http://localhost:8501/)