import pymongo

client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")

mydb = client["Assignment"]

newcol = mydb.Assignment

record = {
            "id" : 1,
            "name":"Lerb",
            "sex":"M",
            "age":18,
            "Province":"SiemReap"
            }

record1 = {
            "id" : 2,
            "name":"Pongthom",
            "sex":"M",
            "age":19,
            "Province":"PhnomPenh"
            }
record2 = {
            "id" : 3,
            "name":"Nguykg",
            "sex":"F",
            "age":23,
            "Province":"PreyVeng"
            }
record3 = [{
            "id" : 4,
            "name":"Cbay",
            "sex":"M",
            "age":15,
            "Province":"SiemReap"   
            },
            {
            "id" : 5,
            "name":"Runback",
            "sex":"F",
            "age":16,
            "Province":"KohKong"   
            },
            {
            "id" : 6,
            "name":"Plaok",
            "sex":"M",
            "age":24,  
            "Province":"Kep"
            }

]

newcol.insert_one(record)
newcol.insert_many([record1,record2])
newcol.insert_many(record3)