import os
import sys
import json
import certifi
import pymongo
import pandas as pd
import numpy as np
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get MongoDB URL
MONGO_DB_URL = os.getenv('MONGO_DB_URL')
print("MongoDB URL:", MONGO_DB_URL)  # Debugging

ca = certifi.where()

class NetworkDataExtract:
    def __init__(self):
        pass

    def csv_to_json(self, file_path):
        try:
            df = pd.read_csv(file_path)
            df.reset_index(drop=True, inplace=True)
            records = list(json.loads(df.T.to_json()).values())
            return records
        except Exception as e:
            print(f"Error in csv_to_json: {e}")
            raise

    def insert_data_mongodb(self, records, database, collection):
        try:
            self.mongdb_client = pymongo.MongoClient(MONGO_DB_URL)
            self.database = self.mongdb_client[database]
            self.collection = self.database[collection]

            if records:
                self.collection.insert_many(records)  # FIXED: Now inserting data

            return len(records)

        except Exception as e:
            print(f"Error in insert_data_mongodb: {e}")
            raise


if __name__ == "__main__":
    FILE_PATH = r'Network_Data\phisingData.csv'  # Fixed path
    DATABASE = 'TALHAAI'
    collection = 'NetworkData'  # Lowercase

    networkobj = NetworkDataExtract()
    records = networkobj.csv_to_json(FILE_PATH)
    print("Records to insert:", records)  # Debugging

    no_of_records = networkobj.insert_data_mongodb(records, DATABASE, collection)
    print(f"Inserted {no_of_records} records successfully.")
