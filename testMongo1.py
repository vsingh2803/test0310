import pymongo
client = pymongo.MongoClient("mongodb+srv://<username>:ShreeRaam12@cluster0.xcmn8lc.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {"name": "vaibhav", "email": "vsingh.2803@yahoo.com","surname": "Singh"}

db1 = client["mongotest"]
coll = db1["test"]
#coll.insert_one(d)