__author__ = 'petermeckiffe'
import Quandl
import matplotlib.pyplot as plt
import matplotlib.dates as md
api_key = 'yyQx6y9SRiVhFo1ukVxt'

mydata = Quandl.get("BCHARTS/KRAKENEUR", authtoken=api_key, trim_start="2013-05-01", trim_end="2015-05-30", )
plt.xticks( rotation=25 )
ax=plt.gca()
xfmt = md.DateFormatter('%Y-%m-%d')
ax.xaxis.set_major_formatter(xfmt)
plt.plot(mydata.index ,mydata['High'], label="High")
plt.plot(mydata.index,mydata['Low'],  label="Low")
plt.plot(mydata.index, mydata['Close'], label="Close")
plt.legend(bbox_to_anchor=(1, 1),
           bbox_transform=plt.gcf().transFigure)
plt.savefig('plotb.png')
#plt.show()