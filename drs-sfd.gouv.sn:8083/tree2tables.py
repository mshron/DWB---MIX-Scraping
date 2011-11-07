#!/usr/bin/env python
from json import loads
from sys import argv

def main():
  h=open(argv[1],'r')
  raw=h.read()
  h.close()
  tree=loads(raw)
  for row in tree:
    page_id=row.pop(0)
    print page_id
    for blob in row:
      #Handle nested elements
      for key in blob.keys():
        if type(blob[key])==type({}):
          for subkey in blob[key].keys():
            if type(blob[key][subkey])==type([]):
              save_with_id([],blob[key].pop(subkey),subkey,page_id)
        elif blob[key]!={}:
          save_with_id([],blob.pop(key),key,page_id)
        else:
          #The element is not nested
          pass
      #Handle non-nested elements
      if len(blob.keys())!=1:
        print len(blob.keys())
        raise UnexpectedChildrenCount
      else:
        save_with_id([],blob.values()[0],blob.keys()[0],page_id)
 
class UnexpectedChildrenCount(Exception):
  pass

def save_with_id(unique,data,name,page_id,unique_id=False):
  if type(data)==type({}):
    data['page_id']=page_id
  elif type(data)==type([]):
    for row in data:
      row['page_id']=page_id
  else:
    raise TypeError
  if unique_id:
    unique.append('page_id')
  save(unique,data,name)

def save(unique,data,name):
  print(unique,data,name)
  #pass

def tableize(row):
#  if
  pass

main()
