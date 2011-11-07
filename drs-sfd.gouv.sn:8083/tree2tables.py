#!/usr/bin/env python
from json import loads
from sys import argv

def main():
  h=open(argv[1],'r')
  raw=h.read()
  h.close()
  tree=loads(raw)
  for row in tree:
    for blob in row:
      #Handle nested elements
      for key in blob.keys():
        if type(blob[key])==type({}):
          for subkey in blob[key].keys():
            if type(blob[key][subkey])==type([]):
              save([],blob[key].pop(subkey),subkey)
        elif blob[key]!={}:
          save([],blob.pop(key),key)
        else:
          #The element is not nested
          pass
      #Handle non-nested elements
      if len(blob.keys())!=1:
        print len(blob.keys())
        raise UnexpectedChildrenCount
      else:
        save([],blob.values()[0],blob.keys()[0])
 
class UnexpectedChildrenCount(Exception):
  pass

def save(unique,data,name):
  #print(unique,data,name)
  pass

def tableize(row):
#  if
  pass

main()
