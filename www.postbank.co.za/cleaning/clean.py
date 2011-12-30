#!/usr/bin/env python

from urllib2 import urlopen
from demjson import encode,decode
import codecs

dump=decode(urlopen('http://chainsaw.iriscouch.com/postbank/_design/clean/_view/all').read())
json=encode([row['key'] for row in dump['rows']])

f=codecs.open('postbank.json','w',encoding='utf-8')
f.write(json)
f.close()
