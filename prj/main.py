
from database import Database
from http.server import HTTPServer
from html_server import Server, database
from pdu import test, database

DB_SERVER_ADDRESS = "localhost"
DB_PORT = 8000

def start_database():
    database.connect_server()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Starting Server')
    server = HTTPServer((DB_SERVER_ADDRESS, DB_PORT), Server)
    try:
        print("Open server on " + DB_SERVER_ADDRESS + " on " + str(DB_PORT))
        server.serve_forever()
    except KeyboardInterrupt:
        print('Stopping server')
        server.socket.close()
    start_database()
    test()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
