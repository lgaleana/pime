from typing import List
from fastapi import FastAPI, HTTPException, Query
from .models import FlightSearch, FlightResult
from .services import search_flights_in_tequila, fetch_flight_details

app = FastAPI()

@app.get('/flights', response_model=List[FlightResult])
def search_flights(
    origin: str = Query(...),
    destination: str = Query(...),
    departure_date: str = Query(...),
    return_date: str = Query(...)
):
    search = FlightSearch(
        origin=origin,
        destination=destination,
        departure_date=departure_date,
        return_date=return_date
    )
    try:
        return search_flights_in_tequila(search)
    except FlightSearchError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get('/flights/{flight_id}', response_model=FlightResult)
def get_flight(flight_id: str):
    try:
        return fetch_flight_details(flight_id)
    except FlightSearchError as e:
        raise HTTPException(status_code=400, detail=str(e))