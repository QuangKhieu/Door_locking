# Import standard modules (libraries of python)
# We must have added the mysql package for the project to work
import mysql.connector
from mysql.connector import errorcode
# Docu: https://dev.mysql.com/doc/connector-python/en/connector-python-examples.html


class Database:
    # Connexion, and cursor (to execute statements to communicate with MYSQL database)
    def __init__(self, database_name):
        self.cnx = None
        self.cursor = None
        self.database_name = database_name

    def get_cnx(self):
        return self.cnx

    def get_cursor(self):
        return self.cursor

    # Connect to the server with a host, port, user and password
    def connect_server(self, has_database_name=False):
        connected = False
        try:
            if has_database_name:
                # And database name
                self.cnx = mysql.connector.connect(user='root', password='', database='users',
                                                   host='localhost', port='3306')
            else:
                self.cnx = mysql.connector.connect(user='root', password='', host='localhost', port='3306')

            self.cursor = self.cnx.cursor()
            # Check if you haven't had any problems up to this line and set connected to true
            connected = True

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password1")
                print(err)
            else:
                print("Failed accessing to database: {}".format(err))
        return connected

    # Close connexion
    def close_server(self):
        # Make sure data is committed to the database
        self.cnx.commit()

        # The close cursor and connexion
        self.cursor.close()
        self.cnx.close()
