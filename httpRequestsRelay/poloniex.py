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
    for key in data.keys():
        print(key)
    
    # print("The response is" +str(data['BTC_SDC']))
    print(data['BTC_SDC']['highestBid'])
    
    
    # In this section highBid and lowAsk are unicode
    highBid  =  data['BTC_SDC']['highestBid']
    lowAsk = data['BTC_SDC']['lowestAsk'];
    
    # In order to sum the values and not all the values for the list we need to convert the vars to floats
    # Float allows us to add the decimal numbers together with precision
    avgBid = (float(highBid) + float(lowAsk)) / 2
    
    # We could just print avgBid but to have a string also we will need to convert to str
    print("This is the btc sdc highest bid "+ highBid)
    print("This is the btc sdc lowest bid "+ lowAsk)
    print("This is the btc sdc avg bid "+ str(avgBid))


    
    return json.dumps(data['BTC_SDC'])
# Run our server everywhere. Can be accessed via the IP of the host computer on port 5000

@app.route('/xmr')
def BTC_XMR():
    r = requests.get('https://poloniex.com/public?command=returnTicker')
    print(r)
    data = r.json()
    for key in data.keys():
        print(key)
    
    # print("The response is" +str(data['BTC_SDC']))
    print(data['BTC_XMR']['highestBid'])
    
    
    # In this section highBid and lowAsk are unicode
    highBid  =  data['BTC_XMR']['highestBid']
    lowAsk = data['BTC_XMR']['lowestAsk'];
    
    # In order to sum the values and not all the values for the list we need to convert the vars to floats
    # Float allows us to add the decimal numbers together with precision
    avgBid = (float(highBid) + float(lowAsk)) / 2
    
    # We could just print avgBid but to have a string also we will need to convert to str
    print("This is the btc sdc highest bid "+ highBid)
    print("This is the btc sdc lowest bid "+ lowAsk)
    print("This is the btc sdc avg bid "+ str(avgBid))

    
    return json.dumps(data['BTC_XMR'])

app.run(debug=False)