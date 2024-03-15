import requests
from typing import List
from .models import FlightSearch, FlightResult
from .exceptions import FlightSearchError

def search_flights_in_tequila(search: FlightSearch) -> List[FlightResult]:
    response = requests.get('http://tequila-api/search', params=search.dict())
    response.raise_for_status()
    return [FlightResult(**flight) for flight in response.json()]

def fetch_flight_details(flight_id: str) -> FlightResult:
    response = requests.get(f'http://tequila-api/flights/{flight_id}')
    response.raise_for_status()
    return FlightResult(**response.json())