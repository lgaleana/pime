import unittest
from unittest.mock import patch
from api.flight_search import flight_search


class TestFlightSearch(unittest.TestCase):
    @patch('requests.get')
    def test_flight_search(self, mock_get):
        mock_get.return_value.json.return_value = {'flights': []}
        result = flight_search({})
        self.assertEqual(result, {'flights': []})
