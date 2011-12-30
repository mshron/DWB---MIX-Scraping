#!/usr/bin/env python
from mechanize import Browser
from urllib2 import urlopen
from lxml.html import fromstring

URL='http://www.postbank.co.za/contact.aspx?ID=3'

def main():
  #for option in options():
  for option in options()[0]:
     b=search(option)
  return b

def options():
  xml=fromstring(urlopen(URL).read())
  select=xml.xpath('//select[@name="Centralcolum3$drpFAQ"]')[0]
  return [(c.attrib['value'],c.text) for c in select.getchildren()][:-1]

def search(option):
  b=_startbrowser(option[0],option[1],save_response='foo.html')
  r=b.click(type="image", nr=1)
  raw=r.read()
  xml=fromstring(raw)
  return b,xml,raw

def _startbrowser(value_id,value,save_response=None):
  b=Browser()
  b.set_handle_referer(False)
  r=b.open(URL)
  if type(save_response)==type('aoeu'):
    out=open(save_response,'w')
    out.write(r.read())
    out.close()

  b.select_form(name='Form1')
  b["Centralcolum3$drpFAQ"]=[value_id]
  b["Centralcolum3$txtown"]=value
  return b

