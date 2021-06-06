from ClientServer import *



def main():
    start_server = ClientServerSocket()
    start_server.server()


if __name__ == '__main__':
    try:
        main()
    except Exception as ans:
        print(ans)
