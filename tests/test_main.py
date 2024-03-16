import unittest
from unittest.mock import patch
from fastapi.testclient import TestClient
from main import app

class TestMain(unittest.TestCase):

    @patch('main.api.search_flights', return_value={'flights': []})
    def test_search(self, mock_search_flights):
        client = TestClient(app)
        response = client.get('/search?fly_from=New York&fly_to=Los Angeles&date_from=2022-12-31&date_to=2022-12-31')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'flights': []})
        mock_search_flights.assert_called_once_with({'fly_from': 'New York', 'fly_to': 'Los Angeles', 'date_from': '2022-12-31', 'date_to': '2022-12-31'})
