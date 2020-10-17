import pymongo as pymongo


class Database:

    URI = "mongodb://127.0.0.1:27017/webstore"
    DATABASE = pymongo.MongoClient(URI).get_database()

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection: str, query: dict):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection: str, query: dict):
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def update(collection: str, query: dict, data: dict):
        Database.DATABASE[collection].update(query, data, upsert=True)

    @staticmethod
    def remove(collection: str, query: dict):
        Database.DATABASE[collection].remove(query)