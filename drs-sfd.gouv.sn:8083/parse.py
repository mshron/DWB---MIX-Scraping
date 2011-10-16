#!/usr/bin/env python
"""
Run this from bash on a directory
containing files from the website.
It will send a list of dicts to stdout.
"""

from lxml.html import fromstring
from sys import argv
from os import listdir

def main():
  datadir=argv[1]
  for f in listdir(datadir):
    print parse(datadir+'/'+f)

def parse(f):
  """Parse a previously downloaded html file"""
  print f
  handle=open(f,'r')
  raw=handle.read()
  handle.close()

  xml=fromstring(raw)
  for tag in xml.xpath('//tr[@class="space"]'):
    xml.remove(tag)
  for tag in xml.xpath('/table[@class="sous-tableau"]'):
    xml.remove(tag)

  cells=xml.xpath('//*[self::th or self::td]')

  #Check for even-ness
  if (len(cells) % 2) != 0:
#    raise AlignmentError
    pass

  d={}
  #while len(cells)>0:
  while len(cells)>1:
    key=cells.pop().text
    value=cells.pop().text
    d[key]=value

  return d

class AlignmentError(Exception):
  pass

if __name__ == '__main__':
  main()
