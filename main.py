from fastapi import FastAPI, Query
import api

app = FastAPI()


@app.get('/search')
def search_flights(params: dict = Query({})): 
    response = api.search_flights(params)
    return response
