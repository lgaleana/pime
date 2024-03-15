import responses
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@responses.activate
def test_search_flights():
    responses.add(responses.GET, 'http://tequila-api/search',
                  json=[{'id': '1', 'origin': 'NYC', 'destination': 'LAX', 'departure_date': '2022-01-01', 'return_date': '2022-01-10', 'price': 200.0}], status=200)

    response = client.get('/flights?origin=NYC&destination=LAX&departure_date=2022-01-01&return_date=2022-01-10')
    assert response.status_code == 200
    assert response.json() == [{'id': '1', 'origin': 'NYC', 'destination': 'LAX', 'departure_date': '2022-01-01', 'return_date': '2022-01-10', 'price': 200.0}]

@responses.activate
def test_get_flight():
    responses.add(responses.GET, 'http://tequila-api/flights/1',
                  json={'id': '1', 'origin': 'NYC', 'destination': 'LAX', 'departure_date': '2022-01-01', 'return_date': '2022-01-10', 'price': 200.0}, status=200)

    response = client.get('/flights/1')
    assert response.status_code == 200
    assert response.json() == {'id': '1', 'origin': 'NYC', 'destination': 'LAX', 'departure_date': '2022-01-01', 'return_date': '2022-01-10', 'price': 200.0}