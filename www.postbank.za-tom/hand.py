#!/usr/bin/env python
from demjson import decode

def main():
  wit=load_har('witspos.har')
  print wit

def load_har(filename):
  h=open(filename,'r')
  har=decode(h.read())
  h.close()
  return har

main()
