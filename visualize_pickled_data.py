__author__ = 'petermeckiffe'
import matplotlib.pyplot as plt
import matplotlib.dates as md
import matplotlib.ticker
import numpy as np
import pickle
import dateutil.parser
mydata = None
with open('stats_pickle', 'rb') as f:
    mydata = pickle.load(open('stats_pickle', 'rb'))
    print(mydata)
    np_data = np.array(mydata)
    dates = md.date2num(list(map(lambda x: dateutil.parser.parse(x), np_data[:,0].tolist())))
    plt.xticks( rotation=25 )
    ax=plt.gca()
    xfmt = md.DateFormatter('%H-%M-%S')
    ax.xaxis.set_major_formatter(xfmt)
    y_formatter = matplotlib.ticker.ScalarFormatter(useOffset=False)
    ax.yaxis.set_major_formatter(y_formatter)
    plt.plot(dates ,np_data[:,1].astype(np.float32))

    plt.savefig('plotc.png')
    #plt.show()