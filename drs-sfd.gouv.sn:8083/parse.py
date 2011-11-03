#!/usr/bin/env python
"""
Run this from bash on a directory
containing files from the website.
It will send a list of dicts to stdout.
"""

from lxml.html import fromstring
from sys import argv
from os import listdir
#from demjson import encode
from json import dumps as encode

def main():
  datadir=argv[1]
  out=argv[2]
  rows=[]
  for f in listdir(datadir):
    row=parse(datadir+'/'+f)
    rows.append(row)
  json=encode(rows)
  o=open(out,'w')
  o.write(json)
  o.close()

def parse(f):
  """Parse a previously downloaded html file"""
  print f
  handle=open(f,'r')
  raw=handle.read()
  handle.close()

  xml=fromstring(raw)
  for tag in xml.xpath('//tr[@class="space"]'):
    xml.remove(tag)
  for tag in xml.xpath('//td[table[@class="sous-tableau"]]'):
    tag.text="sous-tableau"

  cells=[]
  tables=xml.xpath('//div[@class="bloc"]/div/table')[0:3]
  for table in tables:
    cells.extend(table.xpath('tr/*[self::th or self::td]'))

  #Check for even-ness
  if (len(cells) % 2) != 0:
#    raise AlignmentError
    pass

  d={}
  #while len(cells)>0:
  while len(cells)>1:
    key=cells.pop().text
    value=cells.pop().text
    #Catch keys that aren't really keys
    if key==None:
      pass
    else:
      for ws in ('\r','\n','\u00a0'):
        key=key.replace(ws,'')
      if ''!=key and " "!=key[0] and (key not in ('?','NULL')):
        key=key.encode('ascii','replace')
        print key
        d[key]=value

  return d

class AlignmentError(Exception):
  pass

if __name__ == '__main__':
  main()
