import unittest
from unittest.mock import patch
from fastapi.testclient import TestClient
from main import app


class TestMain(unittest.TestCase):

    @patch('main.api.validate_city_name')
    @patch('main.api.search_flights', return_value={'flights': []})
    def test_search(self, mock_search_flights, mock_validate_city_name):
        client = TestClient(app)
        response = client.get('/search?fly_from_city=city1&to_city=city2&date=2022-12-31')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'flights': []})
        mock_validate_city_name.assert_any_call('city1')
        mock_validate_city_name.assert_any_call('city2')
        mock_search_flights.assert_called_once_with({'fly_from': 'city1', 'to': 'city2', 'date': '2022-12-31'})
