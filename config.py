from pymongo import MongoClient

MONGO_URI = "mongodb://loaclhost:27017"
DB_NAME = "mlops_db"
COLLECTION_NAME = "customers"

client = MongoClient(MONGO_URI)
db = MongoClient(MONGO_URI)
collection = db[COLLECTION_NAME]

