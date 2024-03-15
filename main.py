from fastapi import FastAPI, Query
import api

app = FastAPI()


@app.get('/search')
def search_flights(from_city: str = Query(...), to_city: str = Query(...), date: str = Query(...)): 
    params = {'from': from_city, 'to': to_city, 'date': date}
    response = api.search_flights(params)
    return response
