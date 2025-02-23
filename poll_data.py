from send_message import send_message
from apscheduler.schedulers.background import BackgroundScheduler
import atexit
from datetime import datetime
from secrets import token_hex


def search(user_data) -> bool:
    print("Polling data")
    for doc in user_data.find():
        for med in doc['medicine_info']:
            for v in med.values():
                if (not v[1]) and (v[0] == datetime.now().strftime("%w %#H:%M")):
                    key = update_key(user_data, doc['_id'])
                    send_message(key, doc['patient_phone'])
                    return True

    return False


def update_key(user_data, id):
    new_key = token_hex(8)
    user_data.update_one(
        {"_id": id},
        {'$set': {'patient_key': new_key}},
    )
    return new_key


def start_polling(user_data):
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=search, args=[user_data], trigger='interval', seconds=10)
    scheduler.start()
    atexit.register(lambda: scheduler.shutdown())


if __name__ == "__main__":
    start_polling()
