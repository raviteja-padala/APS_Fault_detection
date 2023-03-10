import pymongo
import pandas as pd
import json

from sensor.config import mongo_client

##Provide the mongodb localhost url to connect python to mongodb.
#client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")


DATA_FILE_PATH = "/config/workspace/aps_failure_training_set1.csv"
DATABASE_NAME = "aps06"
COLLECTION_NAME = "sensor"


if __name__ =="__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and Columns in dataset: {df.shape}")

    ##convert data set into json so that we can dump the record into mongo db
    df.reset_index(drop= True, inplace=True)

    json_record = list(json.loads(df.T.to_json()).values())
    #print(json_record[0])

     ##insert converted JSON record to mongo DB
    #client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)

    ## insert into mong atlas using mong client
    mongo_client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
    print("DB inserted")

    


