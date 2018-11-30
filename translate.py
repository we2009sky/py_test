import json
from urllib import request, parse

url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'


head= {}
'''
head['User-Agent'] =  'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
'''
data = {}
content = input('Input translate：')

data['i'] = content
data['from'] = 'AUTO'
data['to'] = 'AUTO'
data['martresult'] = 'dict'
data['client'] = 'fanyideskweb'
data['salt'] = '1532522719505'
data['sign'] = '7f976888452ba382f2e2d97b7fc8c843'
data['doctype'] =  'json'
data['version'] =  '2.1'
data['keyfrom'] = 'fanyi.web'
data['action'] = 'FY_BY_REALTIME'
data['typoResult'] = 'false'

data = parse.urlencode(data).encode('utf-8')

# 为了隐藏User-Agent，不被服务器屏蔽。下两句等价于res = request.urlopen(url, data)
# 也可以用代理
req = request.Request(url, data, head)
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36')

res = request.urlopen(req)

html = res.read().decode('utf-8')

tar = json.loads(html) # html is dict
print ('Your input：',tar['translateResult'][0][0]['src'])
print ('Answer is ：',tar['translateResult'][0][0]['tgt'])

