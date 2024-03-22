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

class TestStatic(unittest.TestCase):

    def test_css_files(self):
        client = TestClient(app)
        response = client.get('/static/css/search.css')
        self.assertEqual(response.status_code, 200)
        self.assertIn('text/css', response.headers['content-type'])
        response = client.get('/static/css/results.css')
        self.assertEqual(response.status_code, 200)
        self.assertIn('text/css', response.headers['content-type'])

    @patch('main.api.search_flights', return_value={'data': mock_flight_data})
    def test_responsive_design(self, mock_search_flights):
        client = TestClient(app)
        response = client.get('/')
        self.assertIn('<meta name=\'viewport\' content=\'width=device-width, initial-scale=1\'>', response.text)
        response = client.get('/search?fly_from=New York&fly_to=Los Angeles&date_from=2022-12-31&date_to=2022-12-31')
        self.assertIn('<meta name=\'viewport\' content=\'width=device-width, initial-scale=1\'>', response.text)
        mock_search_flights.assert_called_once_with({'fly_from': 'New York', 'fly_to': 'Los Angeles', 'date_from': '2022-12-31', 'date_to': '2022-12-31'})