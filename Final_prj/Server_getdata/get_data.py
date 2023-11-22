from Server_getdata.database import Database
import os
import random

DB_SERVER_ADDRESS = "localhost"
DB_PORT = 8000

def start_database():
    database.connect_server()

Test = "test.txt"
# Get Project Name (The name of your folder, you can also change it to a custom name like "Tamagotchi".)
Project_name = os.path.basename(os.getcwd())

# Create the database with tables and correspondent columns
database = Database(Project_name)
# Create two dict types, these can be converted to a JSON
data = {}
response = {}


def create_id(id,ten,tuoi,gt,que):
    global data
    data = {
        "type": "UPDATE",
        'id':id,
        "Ten": ten,
        "Tuoi": tuoi,
        "Gioi Tinh":gt,
        "Que":que
    }

def kiemtra(a):
    global database
    check = False
    if database.connect_server(True):
     query = "SELECT * FROM `quanly`"
     database.cursor.execute(query)
     records = database.cursor.fetchall()
     for (id, b, c, d, e) in records:
        if id==a:
            check = True
            break

    return check


def get_data(id):
    start_database()
    global database, data
    tup = tuple(str(id))
    # Check if an item exist in table items
    if database.connect_server(True):
        if kiemtra(id):
          query = "SELECT * FROM `quanly` WHERE id = %s"
          database.cursor.execute(query,(tup))
          records = database.cursor.fetchall()
          for (id, ten, gt, tuoi, que) in records:
             data = {
              "id": id,
              "Ten": ten,
              "Gioi Tinh": gt,
              "Tuoi": tuoi,
              "Que": que
             }
        database.close_server()
    return data


