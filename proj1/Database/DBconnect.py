from pymongo import MongoClient

# Database connection parameters
DB_HOST = "localhost"
DB_PORT = 27017
DB_USER = "myuser"
DB_PASSWORD = "mypassword"


def connect_and_insert():
    try:
        # Create a MongoDB client
        client = MongoClient(
            f"mongodb://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/"
        )
        db = client.mydatabase
        collection = db.mycollection
        sample_data = {"name": "Alice", "age": 25}
        collection.insert_one(sample_data)

        print("Connected to MongoDB and inserted")

        for doc in collection.find():
            print(doc)

    except Exception as error:
        print("Error connecting to the MongoDB database:", error)
