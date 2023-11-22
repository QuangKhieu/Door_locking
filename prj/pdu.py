from database import Database
import os
from log_info import getjson
import random

Test = "test.txt"
# Get Project Name (The name of your folder, you can also change it to a custom name like "Tamagotchi".)
Project_name = os.path.basename(os.getcwd())

# Create the database with tables and correspondent columns
database = Database(Project_name)

# Create two dict types, these can be converted to a JSON
data = {}
response = {}


def get_data():
    return data


def get_reply():
    return response

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
     for (id,b,c,d,e) in records:
        if id==a:
            check = True
            break

    return check

def Update_data(identifier):
    global database, data
    check = kiemtra(identifier)

    if check:
        add_process_log = ("UPDATE quanly "
                           "SET name = %(Ten)s, "
                           "sex = %(Tuoi)s, age = %(Gioi Tinh)s, home = %(Que)s ",
                           "WHERE id = %(id)s")
        print("Values Changed")
    else:
        add_process_log = ("INSERT INTO quanly(id, name, sex, age,home)"
                           "VALUES (%(id)s, %(Ten)s, %(Tuoi)s, %(Gioi Tinh)s, %(Que)s)")
    database.cursor.execute(add_process_log, data)

def Update_info(identifier, ten, tuoi, gt,que):
    global database
    create_id(identifier, ten, tuoi, gt,que)

    check = False
    if database.connect_server(True):
        query = "SELECT * FROM `quanly` WHERE id = %s"
        database.cursor.execute(query, (identifier,))

        for (ident,) in database.cursor:
            if ident == identifier:
                check = True
                Update_data(identifier)
                break
        database.close_server()
    return check


question = ("Tra loi dung or sai: que la ")
option = ("Dung","Sai")
home = ("HN","HP","BN","BG","LS","HD")


def test():
    global database, data
    a = int(input("nhap dau vao:"))
    tup = tuple(str(a))
    file = open(Test, "a")
    file.truncate(0)
    file.close()
    print(kiemtra(a))
    # Check if an item exist in table items
    if database.connect_server(True):
        if kiemtra(a):
          query = "SELECT * FROM `quanly` WHERE id = %s"
          database.cursor.execute(query,(tup))
          records = database.cursor.fetchall()
          for (id,ten,tuoi,gt,que) in records:
             data = {
              "id":id,
              "Ten": ten,
              "Tuoi": tuoi,
              "Gioi Tinh":gt,
              "Que":que
             }
             file = open(Test, "a")
             text1 = getjson(data)
             file.write(f"{text1}\n")
             file.close()
             b = random.randint(0,5)
             ques = question+home[b]
             print(ques)
             if home[b]==que:
                 ans = "Dung"
             else:
                 ans = "Sai"
             op = input("nhap cau tra loi:")
             if(op==ans):
                 print("OK")
             else:
                 print("Sai")
        database.close_server()

def create_res(code):
    global response
    response = {
        "type": "RES",
        "code": code,
    }

