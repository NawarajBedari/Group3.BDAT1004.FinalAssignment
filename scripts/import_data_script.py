import requests
import time
from database.mongodb_connector import get_mongo_collection
from script_config import Config  # Assuming you have a configuration file

# Function to acquire and store data in MongoDB
def acquire_and_store_data():
    cc_api = "https://data.cityofchicago.org/resource/ijzp-q8t2.json"
    response = requests.get(cc_api)

    if response.status_code == 200:
        data = response.json()
        # Pass the MongoDB URI as an argument to get_mongo_collection
        collection = get_mongo_collection(Config.MONGODB_URI)
        collection.insert_many(data)  # Call insert_many method on the collection object
        print("Data acquired and stored successfully.")
    else:
        print(f"Error: {response.status_code}")

# Run the acquisition process every 24 hours
while True:
    acquire_and_store_data()
    # Wait for 24 hours
    time.sleep(60*60*24)
