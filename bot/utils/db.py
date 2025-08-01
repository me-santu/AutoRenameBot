from pymongo import MongoClient
import os

MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["AutoRenameDB"]
files = db["files"]

def save_file(user_id, filename):
    files.insert_one({"user_id": user_id, "filename": filename})
