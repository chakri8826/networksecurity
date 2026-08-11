
# import os

# from pymongo import MongoClient
# from pymongo.server_api import ServerApi

# uri = os.getenv("MONGO_DB_URL")

# # Create a new client and connect to the server
# client = MongoClient(uri, server_api=ServerApi('1'))

# # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)    


import pymongo

MONGO_DB_URL = "mongodb+srv://kommuchakri8826_db_user:MZEf9GdWvARhtIE3@cluster0.fothodd.mongodb.net"

try:
    client = pymongo.MongoClient(
        MONGO_DB_URL,
        serverSelectionTimeoutMS=10000
    )

    client.admin.command("ping")

    print("MongoDB connection successful!")

except Exception as e:
    print("MongoDB connection failed:")
    print(e)