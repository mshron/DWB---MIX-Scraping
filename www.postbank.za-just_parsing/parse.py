#!/usr/bin/env python

from lxml.html import fromstring
from re import sub

def parse(filename='example.html'):
  xml=loadpage(filename)
  cells=getcells(xml)
  row=makerow(cells)
  print row

def loadpage(filename):
  h=open(filename,'r')
  xml=fromstring(h.read())
  h.close()
  return xml

def getcells(xml):
  table=xml.get_element_by_id('Centralcolum3_dtgGroup')
  cells=table.xpath('descendant::td/*[self::span or self::strong]/text()')
  return cells

def makerow(cells):
  d={}
  d['loc1']=getcellvalue(cells)
  d['loc2']=getcellvalue(cells)
  #End at 2 because there's this junk '1' at the end
  while len(cells)>=2:
    key=getcellvalue(cells)
    value=getcellvalue(cells)
    d[key]=value
  return d

def getcellvalue(cells):
  return compact(cells.pop(0))

def compact(string):
  for char in ('\n','\t'):
    string=string.replace(char,' ')
  for regex in (r'  +',r'^ *',r' *$'):
    string=sub(regex,'',string)
  return string

def _test_compact():
  assert 1==len(compact(' oaeuo     aoeui ').split(' '))

parse()
