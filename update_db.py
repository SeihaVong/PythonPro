import pymongo

client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")

mydb = client["Assignment"]

newcol = mydb.Assignment

# newUpdate = newcol.update_one({"id": 5},{"$set":{"name":"SenRithy"}})

# newUpdateMany = newcol.update_many({"sex":"F"},{"$set":{"sex":"M"}})

cityUpdateMany = newcol.update_many({"Province":"SiemReap"},{"$set":{"Province":"Battambong"}})


