import unittest
from unittest.mock import patch
from fastapi.testclient import TestClient
from main import app

class TestMain(unittest.TestCase):

    @patch('main.api.search_flights', return_value={'data': []})
    def test_search(self, mock_search_flights):
        client = TestClient(app)
        response = client.get('/search?fly_from=New York&fly_to=Los Angeles&date_from=2022-12-31&date_to=2022-12-31')
        self.assertEqual(response.status_code, 200)
        self.assertIn('text/html', response.headers['content-type'])
        mock_search_flights.assert_called_once_with({'fly_from': 'New York', 'fly_to': 'Los Angeles', 'date_from': '2022-12-31', 'date_to': '2022-12-31'})

    @patch('main.api.search_flights', return_value={'data': []})
    def test_results(self, mock_search_flights):
        client = TestClient(app)
        response = client.get('/search?fly_from=New York&fly_to=Los Angeles&date_from=2022-12-31&date_to=2022-12-31')
        self.assertEqual(response.status_code, 200)
        self.assertIn('text/html', response.headers['content-type'])
        mock_search_flights.assert_called_once_with({'fly_from': 'New York', 'fly_to': 'Los Angeles', 'date_from': '2022-12-31', 'date_to': '2022-12-31'})
