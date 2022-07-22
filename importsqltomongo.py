import mysql.connector
import pymongo

client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")


mydb = client["SQLtoDB"]

newcol = mydb.SQLtoDB

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    port="3306",
    database="TIK"
)

cursor = connection.cursor(dictionary = True)


cursor.execute(f"SELECT * FROM dse10" )

students = cursor.fetchall()

if len(students) > 0:
    sqlToMongo = newcol.insert_many(students)
    print(len(sqlToMongo.inserted_ids))