import responses
from app.services import search_flights_in_tequila, fetch_flight_details
from app.models import FlightSearch, FlightResult

@responses.activate
def test_search_flights_in_tequila():
    responses.add(responses.GET, 'http://tequila-api/search',
                  json=[{'id': '1', 'origin': 'NYC', 'destination': 'LAX', 'departure_date': '2022-01-01', 'return_date': '2022-01-10', 'price': 200.0}], status=200)

    search = FlightSearch(origin='NYC', destination='LAX', departure_date='2022-01-01', return_date='2022-01-10')
    result = search_flights_in_tequila(search)
    assert result == [FlightResult(id='1', origin='NYC', destination='LAX', departure_date='2022-01-01', return_date='2022-01-10', price=200.0)]

@responses.activate
def test_fetch_flight_details():
    responses.add(responses.GET, 'http://tequila-api/flights/1',
                  json={'id': '1', 'origin': 'NYC', 'destination': 'LAX', 'departure_date': '2022-01-01', 'return_date': '2022-01-10', 'price': 200.0}, status=200)

    result = fetch_flight_details('1')
    assert result == FlightResult(id='1', origin='NYC', destination='LAX', departure_date='2022-01-01', return_date='2022-01-10', price=200.0)