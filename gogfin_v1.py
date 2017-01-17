import urllib2
import json
import time
import datetime

#https://www.google.com/finance/getprices?q=BANKNIFTY&x=NSE&i=5&f=d,o,h,l,c,v&p=1m
def unixtimeconcerter(time):
    return (datetime.datetime.fromtimestamp(int(time)).strftime('%Y-%m-%d %H:%M:%S')
)

    #self.prefix = "http://finance.google.com/finance/info?client=ig&q="
    #self.prefix = ("https://www.google.com/finance/getprices?q=%s&x=%s&i=60&p=1m&f=d,o,h,l,c" % (symbol,exchange))
def get(symbol,exchange):
    #url = self.prefix+"%s:%s"%(exchange,symbol)
    url = ("https://www.google.com/finance/getprices?q=%s&x=%s&i=60&p=1m&f=d,o,h,l,c" % (symbol,exchange))
    data = {}
    csv = urllib2.urlopen(url).readlines()
    offset,vclose,vhigh,vlow,vopen = csv[7].split(',')
    date = unixtimeconcerter(offset.split('a')[1])
    data["date"] = date
    data["low"] = vlow
    data["open"] = vopen.strip()
    data["close"] = vclose
    data["high"] = vhigh
    print data

if __name__ == "__main__":
    #c = FinanceAPI()
    while 1:
      quote = get("BANKNIFTY", "NSE")
      time.sleep(10)

