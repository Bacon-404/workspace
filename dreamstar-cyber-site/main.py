from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/welcome')
def welcome():
    return render_template('Welcome to Dreamstar Cyber!')

@app.route('sysadmin')
def sysadmin():
    return render_template('Welcome to the Sysadmin page!')

@app.route('cybersecurity')
def cybersecurity():
    return render_template('Welcome to the Cybersecurity page!')

@app.route('/detection_engineering')
def detection_engineering():
    return render_template('Welcome to the Detection Engineering page!')

if __name__ == '__main__':
    app.run()

