from Server_models import *


def test_server()->None:
    start_server = ServerSocket()
    assert start_server.server(True) == (True)
