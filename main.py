from fastapi import FastAPI, Query
import api

app = FastAPI()


@app.get('/search')
def search_flights(from_city: str = Query(None), to_city: str = Query(None), date: str = Query(None)): 
    params = {'from': from_city, 'to': to_city, 'date': date}
    response = api.search_flights(params)
    return response
