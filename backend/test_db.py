from pymongo import MongoClient

MONGODB_URL = "mongodb+srv://eventpilot:Tpmvs*123@eventpilot-cluster.bqkyufo.mongodb.net/?appName=eventpilot-cluster"

try:
    client = MongoClient(MONGODB_URL)
    client.admin.command("ping")
    print("✅ MongoDB Connected Successfully!")
except Exception as e:
    print("❌ Connection Failed")
    print(e)