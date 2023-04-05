from pymongo import MongoClient
from lib.config import mongo_key, mongo_user


#Define connection to the database.
def get_database():

   # Provide the mongodb atlas url to connect python to mongodb using pymongo
   CONNECTION_STRING = f'mongodb+srv://{mongo_user}:{mongo_key}@daft-draft-serverless-0.7f0kwrq.mongodb.net/?retryWrites=true&w=majority'
 
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   client = MongoClient(CONNECTION_STRING)
 
   # Create the database for our example (we will use the same database throughout the tutorial
   return client['Daft_Draft']

      
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":   
  
   # Get the database
   db = get_database()