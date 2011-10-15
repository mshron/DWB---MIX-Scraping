#!/usr/bin/env python
from urllib2 import urlopen
from lxml.html import fromstring
from lxml.etree import tostring

URL='http://www.bancomoc.mz/Instituicoes_en.aspx?id=GINS0017&ling=en'

def main():
  xml=get(URL)
  organizations=xml.xpath('//div[@class="column1-unit"]/h1/div/span/b/font')
  addresses=xml.xpath('//div[@class="column1-unit"]/h1/div/span/font')
  rows=[]
  if len(organizations)!=len(addresses):
    raise AlignmentError
  while len(organizations)>0:
    rows.append({
      "organization":tostring(organizations.pop()).split('<br/>')[1]
    , "address":addresses.pop().text
    })
  print rows

class AlignmentError(Exception):
  pass

def get(url):
  raw=urlopen(url).read()
  return fromstring(raw)

def get_links(xml,xpath='//a',textkey="text",extra={}):
  links=[]
  for a in xml.xpath(xpath):
    if a.text!=None:
      row=copy(extra)
      row[textkey]=a.text
      row["href"]=a.attrib['href']
      links.append(row)
  return links

main()
