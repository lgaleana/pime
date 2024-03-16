from fastapi import FastAPI, Query, Request, HTTPException
from fastapi.templating import Jinja2Templates
import api

app = FastAPI()

templates = Jinja2Templates(directory='templates')

@app.get('/')
def search(request: Request):
    return templates.TemplateResponse('search.html', {'request': request})

@app.get('/search')
def search_flights(fly_from_city: str = Query(...), to_city: str = Query(...), date: str = Query(...)):
    try:
        api.validate_city_name(fly_from_city)
        api.validate_city_name(to_city)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    params = {'fly_from': fly_from_city, 'to': to_city, 'date': date}
    response = api.search_flights(params)
    return response
