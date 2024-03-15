from fastapi import FastAPI

app = FastAPI()

@app.get('/flights')
def search_flights():
    pass
