#!/usr/bin/env python
from urllib2 import urlopen
from lxml.html import fromstring
from lxml.etree import tostring

#from scraperwiki.sqlite import save
def save(unique,data,name):
  """Dummy function"""
  print data

BASEURL='http://www.alafianetwork.org/repimf.php?page='

def main():
  for page in [0]: #range(0,lastpage()+1):
    xml=getpage(page)
    p=xml.xpath('//p[font/strong]')[0]
    d={
      "page":page
    , "table":tostring(table)
    }
    save(['page'],d,'html')

def lastpage():
  xml=getpage(0)
  return int(xml.xpath('//center/a')[-2].text)

def get(url,xml=True):
  html=urlopen(url).read()
  if xml:
    return fromstring(html)
  else:
    return html

def get_file(url,xml=True):
  html=open(url.split('/')[-1]).read()
  if xml:
    return fromstring(html)
  else:
    return html

def getpage(number,xml=True):
  return get_file(BASEURL+str(number),xml)

main()
