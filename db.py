from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
from os import getenv
load_dotenv()

client = MongoClient(getenv('DB_URI'))

try:
    client.admin.command('ping')
    print("Connected to MongoDB!")
except Exception as e:
    print(e)

user_data = client['users']['user_data']

user_model = {
    "client_name": "",
    "client_phone": "",
    "client_email": "",
    "client_password": "",
    "patient_name": "",
    "patient_phone": "",
    "medicine_info": [],
    "food_info": [],
    "plant_status": 0,
    "health_log": [],
    "patient_key": "",
}

if __name__ == "__main__":
    user_model['client_name'] = "John Smith"
    user_model['client_phone'] = "4695920546"
    user_model['client_email'] = "shrekdittakavi@gmail.com"
    user_model['client_password'] = "GardenAid"
    user_model['patient_name'] = "Jane Smith"
    user_model['patient_phone'] = "4695920546"
    user_model['medicine_info'] = [
        {"Tylenol": ["0 1:30 PM", 0]},
        {"Allegra": ["1 7:30 PM", 0]},
        {"Cough syrup": ["1 7:30 PM", 0]},
    ]
    user_model['food_info'] = ["9:30 AM", "1:00 PM", "6:30 PM"]
    user_model['health_log'] = [
        ['2/22/25', '7:30 PM', 'Take medicine', 'Tylenol'],
        ['2/22/25', '7:30 PM', 'Ate dinner', ''],
        ['2/22/25', '1:30 PM', 'Take medicine', 'Allegra'],
        ['2/22/25', '1:30 PM', 'Ate lunch', ''],
    ]
    user_model["patient_key"] = "imp_user"
    user_data.insert_one(user_model)