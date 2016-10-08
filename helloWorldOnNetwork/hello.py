from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

# Run our server everywhere. Can be accessed via the IP of the host computer on port 5000

app.run(host='0.0.0.0')