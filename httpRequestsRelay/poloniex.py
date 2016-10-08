from flask import Flask
import requests

app = Flask(__name__)



@app.route('/')
def hello_world():
    r = requests.get('https://poloniex.com/public?command=returnTicker')
    print(r)
    return r.text.BTC_1CR

# Run our server everywhere. Can be accessed via the IP of the host computer on port 5000

app.run(host='0.0.0.0')