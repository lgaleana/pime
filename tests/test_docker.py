import unittest
from unittest.mock import patch, MagicMock

class TestDocker(unittest.TestCase):
    @patch('docker.from_env')
    def test_build_image(self, mock_docker):
        mock_client = MagicMock()
        mock_docker.return_value = mock_client
        mock_client.images.build.return_value = (MagicMock(), 'build_log')
        image, build_log = mock_client.images.build(path='.')
        self.assertIsNotNone(image, 'Image was not built.')
