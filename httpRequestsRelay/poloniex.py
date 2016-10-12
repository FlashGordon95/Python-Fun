from flask import Flask
from flask import json
import requests

app = Flask(__name__)



@app.route('/')
def hello_world():
    r = requests.get('https://poloniex.com/public?command=returnTicker')
    print(r)
    data = r.json()
    test = [{key} for key in data.keys()]

    # print("The response is" +str(data['BTC_SDC']))
    print(data['BTC_SDC'])

    return "Hello World"
# Run our server everywhere. Can be accessed via the IP of the host computer on port 5000

@app.route('/sdc')
def BTC_SDC():
    r = requests.get('https://poloniex.com/public?command=returnTicker')
    print(r)
    data = r.json()
    test = [{key} for key in data.keys()]
    
    # print("The response is" +str(data['BTC_SDC']))
    print(data['BTC_SDC'])
    
    
    return json.dumps(data['BTC_SDC'])
# Run our server everywhere. Can be accessed via the IP of the host computer on port 5000

@app.route('/xmr')
def BTC_XMR():
    r = requests.get('https://poloniex.com/public?command=returnTicker')
    print(r)
    data = r.json()
    test = [{key} for key in data.keys()]
    print(test)
    
    # print("The response is" +str(data['BTC_SDC']))
    print(data['BTC_XMR'])
    
    return data['BTC_XMR']

app.run(debug=False)