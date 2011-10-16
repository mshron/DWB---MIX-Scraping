#!/usr/bin/env python
from lxml.html import fromstring
from sys import argv
from os import lsdir

def main():
  datadir=argv[1]
  for f in listdir(datadir):
    print parse(f)

def parse(f):
  """Parse a previously downloaded html file"""
  handle=open(f,'r').read()
  raw=fromstring(handle)
  handle.close()

  cells=xml.xpath('//th or td')
  #Check for even-ness
  assert len(cells) % 2 == 0

  d={}
  while len(cells)>0:
    key=cells.pop().text
    value=cells.pop().text
    d[key]=value

  return d

if __name__ == '__main__':
  main()
