from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
from os import getenv
load_dotenv()

client = MongoClient(getenv('DB_URI'), server_api=ServerApi('1'))

try:
    client.admin.command('ping')
    print("Connected to MongoDB!")
except Exception as e:
    print(e)

user_data = client['users']['user_data']

userModel = {
    "client_name": "",
    "patient_name": "",
    "client_phone": "",
    "client_email": "",
    "patient_phone": "",
    "medicine_info": [],
    "food_info": [],
    "plant_status": 0,
    "health_log": [],
}
