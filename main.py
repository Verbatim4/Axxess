from flask import Flask, render_template
# import db

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

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
    return render_template('dashboard.html')


@app.route('/profile/')
def profile():
    return render_template('profile.html')


@app.route('/update/')
def update():
    return render_template('update.html')


if __name__ == "__main__":
    app.run(debug=True, port=1234)
