from datetime import datetime
from pymongo import MongoClient
from bson import ObjectId

from src.config import config

class Database(object):
    def __init__(self):
        print('call database, \n' + str(config))
        self.client = MongoClient(config['db']['url'])
        self.db = self.client[config['db']['name']]

    def count(self, collection_name):
        cnt = self.db[collection_name].count()
        print('count! : ' + str(cnt))
        return cnt

    def insert(self, element, collection_name):
        element["created"] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        element["updated"] = element['created']
        try:
            inserted = self.db[collection_name].insert_one(element)
        except:
            print(datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ' - [database] raise duplicate key error')
            inserted = 'duplicate key error'

        if inserted:
            return inserted
        else:
            print(datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ' - [database] database error')
            return None

    def find(self, criteria, collection_name, projection=None, sort=None, skip=0, limit=0, cursor=False):
        if "_id" in criteria:
            criteria["_id"] = ObjectId(criteria["_id"])

        found = self.db[collection_name].find(filter=criteria, projection=projection, skip=skip, limit=limit, sort=sort)

        if cursor:
            return found

        found = list(found)

        for i in range(len(found)):
            if "_id" in found[i]:
                found[i]["_id"] = str(found[i]["_id"])

        return found

    def find_by_id(self, id, collection_name):
        found = self.db[collection_name].find_one({"_id": ObjectId(id)})

        if found is None:
            return not found
        if "_id" in found:
            found["_id"] = str(found["_id"])

        return found

    def update(self, id, element, collection_name):
        criteria = {"_id": ObjectId(id)}

        element["updated"] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        set_obj = {"$set": element} # update value

        updated = self.db[collection_name].update_one(criteria, set_obj)
        if updated.matched_count == 1:
            # return "Record Successfully Updated"
            return id
        else:
            return None

    def delete(self, id, collection_name):
        print(collection_name)
        print(id + ', ')
        deleted = self.db[collection_name].delete_one({"_id": ObjectId(id)})
        return bool(deleted.deleted_count)



