from time import sleep

from Server_models import *


def main():
    ' did two functions. One start one not start'
    test_error_server()
    test_server()


def test_error_server():
    start_server = ServerSocket()
    assert start_server.server('test','ttt') == 'Все ОК'


def test_server():
    start_server = ServerSocket()
    assert start_server.server('test') == 'Все ОК'


if __name__ == '__main__':
    try:
        main()
    except Exception as ans:
        print(ans)
