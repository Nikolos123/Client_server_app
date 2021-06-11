from Client_models import *


def main():
    "did three functions  the one no start"
    test_client()
    test_auth_client()
    test_client_error()


def test_client():
    name = 'Nikolay'
    password = '1111'
    start_client = ClientSocket()
    assert start_client.client('', name, password, 'test') == ('Все ОК')


def test_auth_client():
    name = 'Nil'
    password = '1111'
    start_client = ClientSocket()
    start_client.client('', name, password, 'test')
    assert start_client.client('', name, password, 'test') == ('Все ОК')


def test_client_error():
    name = 'Nikolay'
    password = '1111'.encode('utf-8')

    start_client = ClientSocket()
    assert start_client.client() == ('Все ОК')


if __name__ == '__main__':
    try:
        main()
    except Exception as ans:
        print(ans)
