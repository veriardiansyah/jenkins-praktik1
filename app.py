from flask import flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Jenkins Multibranch Pipeline!"

if __name__ =='__master__':
    app.run(host='0.0.0.0', port=5000)
