from pymongo import MongoClient

try:
    client = MongoClient("mongodb+srv://vasusingh1305:Delhi123@tncsummarizer.kxrcp0j.mongodb.net/?retryWrites=true&w=majority&appName=TnCSummarizer", serverSelectionTimeoutMS=5000)
    db = client["tnc_db"]
    summaries = db["summaries"]
    print("✅ MongoDB connected successfully")
except Exception as e:
    print(f"⚠️ MongoDB connection failed: {e}")
    print("⚠️ Running without database - summaries will not be cached")
    summaries = None
