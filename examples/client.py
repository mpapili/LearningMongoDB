from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('localhost', 27017)

# Choose database
db = client['yourDatabaseName']

# Choose collection
collection = db['yourCollection']

# Insert a document
collection.insert_one({"name": "John Doe"})

# Query the collection
for doc in collection.find():
    print(doc)

