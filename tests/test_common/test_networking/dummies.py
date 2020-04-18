
from client.client import Client
from server.server import Server


def get_dummy_client():
    return Client(use_dummy=True)


def get_dummy_server():
    return Server(use_dummy=True)
