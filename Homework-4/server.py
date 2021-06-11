from Server_models import *



def main():
    start_server = ServerSocket()
    start_server.server()


if __name__ == '__main__':
    try:
        main()
    except Exception as ans:
        print(ans)
