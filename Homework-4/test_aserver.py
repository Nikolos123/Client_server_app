from time import sleep

from ClientServer import *


def main():
    test_error_server()
    test_server()


def test_error_server():
    start_server = ClientServerSocket()
    start_server.server('11', 'eqwe')


def test_server():
    start_server = ClientServerSocket()
    start_server.server()


if __name__ == '__main__':
    try:
        main()
    except Exception as ans:
        print(ans)
