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
    row=parse(datadir+'/'+f,localisation)
    rows.append(row)
  json=encode(rows)
  o=open(out,'w')
  o.write(json)
  o.close()


def treeify(xml):
  blocs=xml.xpath('//div[@class="bloc"]')
  for bloc in blocs:
    bloc_key=bloc.xml('h3[@class="detail-title"]/text()')[0]
    bloc_child=bloc.xml('div/table')
    for tr in bloc_child.xpath('tr')
      if not has_subtable(tr):
        for th in tr.xpath('th')
          key=th.text
          value=th.getnext().text
          #Then write the dict
      else:
        subtable=get_subtable(tr)


def has_subtable(tr):
  return len(_get_subtables(tr))==1:

def get_subtable(tr):
  return _get_subtables(tr)[0]

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


def conditionalities(xml):
  """This table is actually a decently structured tree;
  you get the bizarre single-column rows if you have grouped (nested)
  information. I could parse this systematically. Do that."""
  cond=xml.xpath('//div[@class="detail detail-2"]/table')
  return cond

def financial_sectors(cond):
  ths=cont.xpath('tr/td[@colspan="4"]/table[@class="sous-tableau"]/tr/th')
  d={}
  for th in ths:
    td_query=th.getparent().getnext().xpath('td')
    if 1==len(td_query):
      td=td_query[0]
    else:
      raise AlignmentError
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

def parse(f,get_node_list):
  """Parse a previously downloaded html file"""
  #print f
  handle=open(f,'r')
  raw=handle.read()
  handle.close()

  xml=fromstring(raw)
  d=get_node_list(xml)
  return d

class AlignmentError(Exception):
  pass

if __name__ == '__main__':
  main()
