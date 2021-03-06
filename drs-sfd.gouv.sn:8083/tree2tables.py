#!/usr/bin/env python
from json import loads,dumps
#from demjson import encode as dumps
from sys import argv

tables={}

def main():
  h=open(argv[1],'r')
  raw=h.read()
  h.close()
  tree=loads(raw)
  for row in tree:
    page_id=row.pop(0)
    #print page_id
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
        #print len(blob.keys())
        raise UnexpectedChildrenCount
      else:
        save_with_id([],blob.values()[0],blob.keys()[0],page_id)
  write_tables()
 
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
  #print(unique,data,name)
  if not name in tables.keys():
    tables[name]=[]

  table=tables[name]

  if type(data)==type([]):
    table.extend(data)
  elif type(data)==type({}):
    table.append(data)

def write_tables():
  for key in tables.keys():
    table=tables[key]
    #print table
    if table!=[]:
      json=dumps(table)
      cleankey=key.encode('ascii','ignore').replace(' ','').replace(':','')
      out=open('tables/'+cleankey+'.json','w')
      out.write(json)
      out.close()

def tableize(row):
#  if
  pass

main()
