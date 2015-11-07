from pymongo import MongoClient

class Database:

    def __init__(self, url):
        self.cli = MongoClient(url)
        self.db = self.cli.get_default_database()
        self.coll = self.db[self.db.name]

    def create(self, item):
        self.coll.insert_one(item)

    def find_all(self):
        return [item for item in self.coll.find(projection={'_id': False})]

    def clear(self):
        self.coll.drop()
