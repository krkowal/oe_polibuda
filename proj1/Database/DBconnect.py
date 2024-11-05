from pymongo import MongoClient

# Database connection parameters
DB_HOST = "localhost"
DB_PORT = 27017
DB_USER = "myuser"
DB_PASSWORD = "mypassword"


def connect_and_insert(data):
    try:
        client = MongoClient(
            f"mongodb://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/"
        )
        db = client.mydatabase
        collection = db.mycollection
        sample_data = {"Final Value": data}
        collection.insert_one(sample_data)

        print("Connected to MongoDB and inserted")

        for doc in collection.find():
            print(doc)

    except Exception as error:
        print("Error connecting to the MongoDB database:", error)
