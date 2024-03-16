import unittest
from unittest.mock import patch
from fastapi.testclient import TestClient
from main import app

mock_flight_data = [
    {
        'cityFrom': 'New York',
        'cityTo': 'Los Angeles',
        'local_departure': '2022-12-31T00:00:00',
        'local_arrival': '2022-12-31T12:00:00',
        'duration': {'total': 7200},
        'price': 500,
        'airlines': ['AA']
    }
]

class TestMain(unittest.TestCase):

    @patch('main.api.search_flights', return_value={'data': []})
    def test_search(self, mock_search_flights):
        client = TestClient(app)
        response = client.get('/search?fly_from=New York&fly_to=Los Angeles&date_from=2022-12-31&date_to=2022-12-31')
        self.assertEqual(response.status_code, 200)
        self.assertIn('text/html', response.headers['content-type'])
        mock_search_flights.assert_called_once_with({'fly_from': 'New York', 'fly_to': 'Los Angeles', 'date_from': '2022-12-31', 'date_to': '2022-12-31'})

    @patch('main.api.search_flights', return_value={'data': mock_flight_data})
    def test_search_flights_results(self, mock_search_flights):
        client = TestClient(app)
        response = client.get('/search?fly_from=New York&fly_to=Los Angeles&date_from=2022-12-31&date_to=2022-12-31')
        self.assertEqual(response.status_code, 200)
        self.assertIn('text/html', response.headers['content-type'])
        for flight in mock_flight_data:
            self.assertIn(flight['cityFrom'], response.text)
            self.assertIn(flight['cityTo'], response.text)
            self.assertIn(flight['local_departure'], response.text)
            self.assertIn(flight['local_arrival'], response.text)
            self.assertIn(str(flight['duration']['total']), response.text)
            self.assertIn(str(flight['price']), response.text)
            self.assertIn(flight['airlines'][0], response.text)
        mock_search_flights.assert_called_once_with({'fly_from': 'New York', 'fly_to': 'Los Angeles', 'date_from': '2022-12-31', 'date_to': '2022-12-31'})