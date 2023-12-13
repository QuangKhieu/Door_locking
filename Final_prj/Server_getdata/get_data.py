from Server_getdata.database import Database
import os
#
#
# DB_SERVER_ADDRESS = "localhost"
# DB_PORT = 8000
#
# def start_database():
#     database.connect_server()
# # Get Project Name (The name of your folder, you can also change it to a custom name like "listfinger".)
# Project_name = os.path.basename(os.getcwd())
#
# # Create the database with tables and correspondent columns
# database = Database(Project_name)
# # Create two dict types, these can be converted to a JSON
# data = {}
# response = {}
#
# def kiemtra(a):
#     global database
#     check = False
#     if database.connect_server(True):
#      query = "SELECT * FROM `listfinger`"
#      database.cursor.execute(query)
#      records = database.cursor.fetchall()
#      for (id,ten,que,q1,a1,q2,a2,q3,a3) in records:
#         if id==a:
#             check = True
#             break
#
#     return check
#
# def get_data(id):
#     start_database()
#     global database, data
#     tup = tuple(str(id))
#     # Check if an item exist in table items
#     if database.connect_server(True):
#         if kiemtra(id):
#           query = "SELECT * FROM `listfinger` WHERE id = %s"
#           database.cursor.execute(query,(tup))
#           records = database.cursor.fetchall()
#           for (id, ten, que, q1, a1, q2, a2, q3, a3) in records:
#              data = {
#               "id": id,
#               "Ten": ten,
#               "Que":que,
#               "Q1": q1,
#               "Ans1":a1,
#               "Q2": q2,
#               "Ans2": a2,
#               "Q3": q3,
#               "Ans3":a3
#              }
#         database.close_server()
#         resultlist = list(data.values())
#     return resultlist
# from database import Database
# import os
# import random

DB_SERVER_ADDRESS = "localhost"
DB_PORT = 8000

def start_database():
    database.connect_server()

Test = "test.txt"
# Get Project Name (The name of your folder, you can also change it to a custom name like "listfinger".)
Project_name = os.path.basename(os.getcwd())

# Create the database with tables and correspondent columns
database = Database(Project_name)
# Create two dict types, these can be converted to a JSON
data = {}
response = {}

def kiemtra(a):
    global database
    check = False
    if database.connect_server(True):
     query = "SELECT * FROM `listfinger`"
     database.cursor.execute(query)
     records = database.cursor.fetchall()
     for (id,ten,que,q1,a1,q2,a2,q3,a3) in records:
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
          query = "SELECT * FROM `listfinger` WHERE id = %s"
          database.cursor.execute(query,(tup))
          records = database.cursor.fetchall()
          for (id,ten,que,q1,a1,q2,a2,q3,a3) in records:
             data = {
              "id":id,
              "Ten": ten,
              "Que":que,
              "Q1": q1,
              "Ans1":a1,
              "Q2": q2,
              "Ans2": a2,
              "Q3": q3,
              "Ans3":a3
             }
        database.close_server()
    resultlist = list(data.values())
    return resultlist



