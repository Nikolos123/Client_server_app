from Client_models import *


def test_client_401() -> None:
    name = 'Nil'
    password = '1111'
    start_client = ClientSocket()
    assert start_client.client('', name, password) == (401)


def test_client_error() -> None:
    name = 'Nikolay'
    password = '1111'
    start_client = ClientSocket()
    assert start_client.client('', name, password) == (201)


def test_client_200() -> None:
    name = 'Nikolay'
    password = '1111'
    start_client = ClientSocket()
    assert start_client.client('', name, password) == (200)
