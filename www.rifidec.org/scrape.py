#!/usr/bin/env python

import urls

def main():
  regions,orgs=urls.urls()
  save(regions,'regions.csv')
  save(orgs,'orgs.csv')
  for org in orgs:
    xml=urls.get(urls.URLS['base']+org['href'])
    org.update(dig(xml))
  print len(orgs)

def save(foo,name):
  """Dummy function for now"""
  print(foo)

def dig(xml):
  """Dig for data"""
  d={}
  values=xml.xpath('//p/span')
  for v in values:
    key=v.getparent().text
    value=v.text
    d[key]=value
  return d

def test_one_url():
  xml=urls.get('http://www.rifidec.org/membres/kin_mec_bosangani.htm')
  print dig(xml)

if __name__ == '__main__':
  main()
#  test_one_url()
