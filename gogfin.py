import urllib2
import json
import time

class FinanceAPI:
  def __init__(self):
    self.prefix = "http://finance.google.com/finance/info?client=ig&q="
  def get(self,symbol,exchange):
    url = self.prefix+"%s:%s"%(exchange,symbol)
    u = urllib2.urlopen(url)
    content = u.read()

    obj = json.loads(content[3:])
    return obj[0]

if __name__ == "__main__":
    c = FinanceAPI()
    while 1:
      quote = c.get("NSE","BANKNIFTY")
      print quote
      time.sleep(05)

