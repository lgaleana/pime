from fastapi import FastAPI
import api

app = FastAPI()


@app.get('/search')
def search_flights():
    params = {}
    response = api.search_flights(params)
    return response
