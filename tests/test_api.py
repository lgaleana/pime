import unittest
from unittest.mock import patch
import api


class TestApi(unittest.TestCase):
    @patch('requests.get')
    def test_search_flights(self, mock_get):
        mock_get.return_value.json.return_value = {'flights': []}
        result = api.search_flights({})
        self.assertEqual(result, {'flights': []})
