from flask import Flask, render_template, request
from db import user_data
from poll_data import start_polling

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login/')
def login():
    return render_template('auth/login.html')


@app.route('/register/')
def register():
    return render_template('auth/register.html')


@app.route('/setup/')
def setup():
    return render_template('auth/setup.html')


@app.route('/dashboard/')
def dashboard():
    user = user_data.find_one({"patient_key": "00000000"})
    return render_template(
        'dashboard.html', 
        logs=user['health_log'], 
        food=user['food_info'],
        name=user['patient_name'],
    )


@app.route('/profile/')
def profile():
    return render_template('profile.html')


@app.route('/update/')
def update():
    return render_template('update.html')


@app.route('/patient/')
def patient_blank():
    return render_template('patient_error.html')

@app.route('/patient/<key>')
def patient(key):
    if not key:
        return render_template('patient_error.html')
    
    document = user_data.find_one({"patient_key": key})
    if document:
        meds = [list(i.keys())[0] for i in document['medicine_info']]
        return render_template('patient.html', meds=meds, food=document['food_info'])

    return render_template('patient_error.html')

    
if __name__ == "__main__":
    # start_polling(user_data)
    app.run(debug=True, port=1234, use_reloader=False)
