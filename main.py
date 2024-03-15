from fastapi import FastAPI, Query, Request
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
import api
import os

load_dotenv()

app = FastAPI()

templates = Jinja2Templates(directory='templates')

@app.get('/')
def search(request: Request):
    return templates.TemplateResponse('search.html', {'request': request})

@app.get('/search')
def search_flights(from_city: str = Query(...), to_city: str = Query(...), date: str = Query(...)):
    params = {'from': from_city, 'to': to_city, 'date': date, 'apikey': os.getenv('TEQUILA_API_KEY')}
    response = api.search_flights(params)
    return response
