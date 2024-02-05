from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/interest-areas')
def interest_areas():
    return render_template('interest-areas.html')

@app.route('/interest-areas/sysadmin')
def sysadmin():
    return 'Welcome to the Sysadmin page!'

@app.route('/interest-areas/cybersecurity')
def cybersecurity():
    return 'Welcome to the Cybersecurity page!'

@app.route('/interest-areas/detection_engineering')
def detection_engineering():
    return 'Welcome to the Detection Engineering page!'

if __name__ == '__main__':
    app.run()

