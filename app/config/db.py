from pymongo import MongoClient

uri = "mongodb+srv://panorama:panorama545@panoramameasurement.8ltjg.mongodb.net/?retryWrites=true&w=majority&appName=PanoramaMeasurement"

client = MongoClient(uri)

db = client.PanoramaMeasurement

users_collection = db["Users"]
