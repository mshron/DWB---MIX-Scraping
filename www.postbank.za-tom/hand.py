#!/usr/bin/env python
from demjson import decode
from requests import post

def main():
  pass
  #print wit['request'].keys()

def grab(identifier):
  wit=load_har('witspos.har')
  print 'Loaded the HAR'
  response=post(
    url=wit['url']
  , data=wit['params']
  , headers=wit['headers']
  )
  print 'Sent the request'
  print response.content

def load_har(filename):
  """Load a HAR file from which we'll determine the requests."""
  h=open(filename,'r')
  har=decode(h.read())
  h.close()
  out={
    "url":har['request']['url']
  , "headers":dictionarify(har['request']['headers'])
  , "params":dictionarify(har['request']['postData']['params'])
  }
  return out

def dictionarify(harlist):
  out={}
  for pair in harlist:
    out[pair['name']]=pair['value']
  return out

grab(23)
