import urllib.request
import re
def getline():
    url = "http://www.lotteryusa.com/powerball/pb-year.html"  
    headers = {}
    headers['User-Agent'] ="Mozilla/5.0 (X11; Linux i686)AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    values = {'s':'basic','submit':'search'}
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')
    req = urllib.request.Request(url, headers = headers)
    resp = urllib.request.urlopen(req)
    respData = resp.read()
    ##print(respData)
    scribe = open('pwrballSource.txt','w+')
    scribe.write (str(respData))
    scribe.close()
    
def update():
    getline()
