import unittest
from unittest.mock import patch
from fastapi.testclient import TestClient
from main import app

class TestStatic(unittest.TestCase):

    def test_css_files(self):
        client = TestClient(app)
        response = client.get('/static/css/search.css')
        self.assertEqual(response.status_code, 200)
        self.assertIn('text/css', response.headers['content-type'])
        response = client.get('/static/css/results.css')
        self.assertEqual(response.status_code, 200)
        self.assertIn('text/css', response.headers['content-type'])

    @patch('main.api.search_flights', return_value={'data': []})
    def test_responsive_design(self, mock_search_flights):
        client = TestClient(app)
        response = client.get('/static/css/search.css')
        self.assertIn('@media (max-width: 600px)', response.text)
        response = client.get('/static/css/results.css')
        self.assertIn('@media (max-width: 600px)', response.text)
        response = client.get('/search?fly_from=New York&fly_to=Los Angeles&date_from=2022-12-31&date_to=2022-12-31')
        self.assertIn('<div style=\'overflow-x: auto;\'>', response.text)
        mock_search_flights.assert_called_once_with({'fly_from': 'New York', 'fly_to': 'Los Angeles', 'date_from': '2022-12-31', 'date_to': '2022-12-31'})
