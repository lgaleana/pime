from fastapi import FastAPI, Query, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import api

app = FastAPI()

app.mount('/static', StaticFiles(directory='static'), name='static')

templates = Jinja2Templates(directory='templates')

@app.get('/')
def search(request: Request):
    return templates.TemplateResponse('search.html', {'request': request})

@app.get('/search')
def search_flights(request: Request, fly_from: str = Query(...), fly_to: str = Query(...), date_from: str = Query(...), date_to: str = Query(...)):
    params = {'fly_from': fly_from, 'fly_to': fly_to, 'date_from': date_from, 'date_to': date_to}
    response = api.search_flights(params)
    return templates.TemplateResponse('results.html', {'request': request, 'flights': response['data']})