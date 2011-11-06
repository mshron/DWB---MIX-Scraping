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

def save(unique,data,name):
  print(unique,data,name)

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

def treeify(xml):
  bloc_nodes=xml.xpath('//div[@class="bloc"]')
  blocs=[]

  for bloc in bloc_nodes:
    bloc_key=bloc.xpath('h3[@class="detail-title"]/text()')[0]
    child=bloc.xpath('div/table')[0]
    for tr in child.xpath('tr'):
      if not has_subtable(tr):
        bloc_l1={}
        for th in tr.xpath('th'):
          key=th.text
          value=th.getnext().text
          bloc_l1[key]=value
      else:
        subtable=get_subtable(tr)
        key=get_subtable_key(tr)
        bloc_l1[key]=detable(subtable)
        
    bloc_l0={bloc_key:bloc_l1}
    blocs.append(bloc_l0)
    return blocs

def detable(subtable):
  colnames=subtable.xpath('tr[position()=1]/th/text()')
  row_nodes=subtable.xpath('tr[position()>1]')
  row_list=[]
  for row in row_nodes:
    d_row={}
    for key,value in zip(colnames,row.xpath('td/text()')):
      d_row[key]=value
    row_list.append(d_row)
  return row_list

def has_subtable(tr):
  return len(_get_subtables(tr))==1

def get_subtable(tr):
  return _get_subtables(tr)[0]

def get_subtable_key(tr):
  return tr.xpath('th[position()=1]/text()')[0]

def _get_subtables(tr):
  subtables=tr.xpath('tr[colspan="4"]/table[@class="sous-tableau"]')
  return subtables



def location(xml):
  ths=xml.xpath('//div[@class="detail detail-1"]/table/tr/th')
  d={}
  for th in ths:
    td=th.getnext()
    d.update({th.text:td.text})
  return d


def check_evenness(nodes):
  """Check for even-ness."""
  if (len(nodes) % 2) != 0:
    raise AlignmentError

def clean_text(text):
  for ws in ('\r','\n','\u00a0'):
    text=text.replace(ws,'')
  if ''!=key and " "!=key[0] and (key not in ('?','NULL')):
    text=text.encode('ascii','replace')
  return text

def parse(f):
  """Parse a previously downloaded html file"""
  #print f
  handle=open(f,'r')
  raw=handle.read()
  handle.close()

  xml=fromstring(raw)
  return treeify(xml)

class AlignmentError(Exception):
  pass

if __name__ == '__main__':
  main()
