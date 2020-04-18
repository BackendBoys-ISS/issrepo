import unittest
import common.networking.requests as req
from tests.test_common.test_networking.dummies import get_dummy_client, get_dummy_server


class TestCommunication(unittest.TestCase):

    def setUp(self) -> None:
        self.client = get_dummy_client()
        self.server = get_dummy_server()

    def test_echo(self):
        response = self.client.send_request(req.Echo("Meow meow meow"))
        print(response.__dict__)
        self.assertTrue(response.was_successful())
        self.assertEqual(response.response_from_server, 'server response')
