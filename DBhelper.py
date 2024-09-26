from pymongo import MongoClient, errors
from bson.objectid import ObjectId

class DBHelper:
    def __init__(self):
        try:
            # Use actual password, and preferably use environment variables for security
            self.client = MongoClient('mongodb+srv://zeeshanaftababbasi:8gM36w2eUuFsRrUM@pythonwithmongobd.lbhv5.mongodb.net/',
                                )
            # The connection is automatically established on instantiation, no need for client.connect()
            # Try pinging the server to confirm connection
            self.client.admin.command('ping')
            self.db=self.client['YouTube_Manager']
            print("Connection Successful")
        except errors.ConnectionFailure as e:
            print(f"Connection failed: {e}")
        except Exception as e:
            print(f"Some error occurred: {e}")

    def Insert(self,name,time,link):
        try:
            self.db.Videos.insert_one({"name" : name,"time":time,"link":link})
            return 1
        except errors as e:
            print(f'Error Occured as {e}')
    def Update(self,name,time,link,id):
        try:
            self.db.Videos.update_one({"_id" : ObjectId(id)},
                                  {'$set':{"name":name,"time":time,"link":link}}
                                  )
            return 1
        except errors as e:
            print(f'Error Occured as {e}')
    def Delete(self,id):
        try:
            self.db.Videos.delete_one({'_id':ObjectId(id)})
            return 1
        except errors as e:
            print(f'Error Occured as {e}')
    def Display(self,id):
        try:
            data=self.db.Videos.find_one({'_id':ObjectId(id)})
            return data
        except errors as e:
            print(f'Error Occured as {e}')
    

