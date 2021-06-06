from ClientServer import *

def main():
    test_client()
    test_auth_client()
    test_client_error()


def test_client():
        name = 'Nikolay'
        password = '1111'
        start_client = ClientServerSocket()
        start_client.client('', name, password)


def test_auth_client():
        name = 'Nil'
        password = '1111'
        start_client = ClientServerSocket()
        start_client.client('', name, password)

def test_client_error():

    name = 'Nikolay'
    password = '1111'.encode('utf-8')

    start_client = ClientServerSocket()
    start_client.client()

if __name__ == '__main__':
    try:
        main()
    except Exception as ans:
        print(ans)