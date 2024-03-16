import unittest
from unittest.mock import patch
from fastapi.testclient import TestClient
from main import app


class TestMain(unittest.TestCase):

    @patch('main.api.search_flights', return_value={'flights': []})
    def test_search(self, mock_search_flights):
        client = TestClient(app)
        response = client.get('/search?fly_from_city=New York&to_city=Los Angeles&date=2022-12-31')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'flights': []})
        mock_search_flights.assert_called_once_with({'fly_from': 'New York', 'to': 'Los Angeles', 'date': '2022-12-31'})
