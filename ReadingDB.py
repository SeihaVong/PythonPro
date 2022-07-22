import pymongo

client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")

mydb = client["Assignment"]

newcol = mydb.Assignment

cursor = newcol.find()

for record in cursor:
    
    print(record)

