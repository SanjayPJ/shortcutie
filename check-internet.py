import urllib.request
import time

def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host) #Python 3.x
        return True
    except:
        return False
# test
print( 'Internet is connected.' if connect() else 'no internet!' )
time.sleep(2)
