__author__ = 'petermeckiffe'
import urllib.request
import json
import pickle
import os
try:
    os.remove('stats_pickle')
except:
    pass

from twisted.internet import task
from twisted.internet import reactor

timeout = 60.0 # Sixty seconds

def doWork():
    request = "https://api.coindesk.com/v1/bpi/currentprice/GBP.json"
    with urllib.request.urlopen(request) as response:
        str_response = response.read().decode('utf-8')
        obj = json.loads(str_response)
        important_info = [obj['time']['updatedISO'], obj['bpi']['GBP']['rate_float']]
        pickle_fn = os.path.join(os.path.dirname(__file__), '../resources/stats_pickle')
        mydata = None
        try:
            mydata = pickle.load(open(pickle_fn, 'rb'))
        except:
            pass

        if mydata is None:
            mydata = list()
        mydata.append(important_info)
        with open(pickle_fn, 'wb') as f:
            pickle.dump(mydata,f)

l = task.LoopingCall(doWork)
l.start(timeout) # call every sixty seconds

reactor.run()