#!/usr/bin/env python
from urllib2 import urlopen
from lxml.html import fromstring

#from scraperwiki.sqlite import save
def save(unique,data,name):
  """Dummy function"""
  print data

BASEURL='http://www.alafianetwork.org/repimf.php?page='

def main():
  for p in [0]: #range(0,lastpage()+1):
    xml=getpage(p)
    print xml.xpath('//p')

def lastpage():
  xml=getpage(0)
  return int(xml.xpath('//center/a')[-2].text)

def get(url):
  return fromstring(urlopen(url).read())

def get_file(url):
  return fromstring(open(url.split('/')[-1]).read())

def getpage(number):
  return get_file(BASEURL+str(number))

main()
