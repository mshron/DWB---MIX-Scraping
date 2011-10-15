#!/usr/bin/env python

from copy import copy

from urllib2 import urlopen
from lxml.html import fromstring

URLS={
  "base":"http://www.rifidec.org/membres/"
}

def urls():
  regions=[]
  orgs=[]
  region_id=0
  for url in region_urls():
    region_id=region_id+1
    xml=get(URLS['base']+url['href'])

    #Regions row
    regions.append({
      "region_id":region_id
    , "region":url['region']
    })
    #print regions

    #Organization rows
    orgs.extend(get_links(
      xml
#    , '//table/tr/td/a'
    , '//a'
    , textkey="organization"
    , extra={"region_id":region_id}
    )[:-1])
    #print orgs

  return [regions,orgs]

def get(url):
  raw=urlopen(url).read()
  return fromstring(raw)

def region_urls():
  xml=get('http://www.rifidec.org/membres/infomembres.htm')
  return get_links(xml,'//a',textkey="region")[:-1]

def get_links(xml,xpath='//a',textkey="text",extra={}):
  links=[]
  for a in xml.xpath(xpath):
    if a.text!=None:
      row=copy(extra)
      row[textkey]=a.text
      row["href"]=a.attrib['href']
      links.append(row)
  return links

if __name__ == '__main__':
  regions,orgs=urls()
  print regions
