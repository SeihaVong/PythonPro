import pymongo

client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")

mydb = client["Assignment"]

newcol = mydb.Assignment

newDelete = newcol.delete_one({"id": 1})

newUpdate = newcol.delete_many({}) 

newDelete = newcol.delete_many({"sex": "F"})
