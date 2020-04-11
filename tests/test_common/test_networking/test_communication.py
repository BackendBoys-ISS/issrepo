import unittest

from tests.test_common.test_networking.dummies import get_dummy_request, get_dummy_sender, get_dummy_server


class TestCommunication(unittest.TestCase):

    def setUp(self) -> None:
        self.request = get_dummy_request()
        self.request_sender = get_dummy_sender()
        self.server = get_dummy_server()

    def test_echo(self):
        response = self.request_sender.send_request_to_server(self.request)
        self.assertTrue(response.was_successful())
