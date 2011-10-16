'''Takes the json file on arg[1], which hopefully has an 'address' column, geocodes it, writes out to arg[2]'''

from geocodeAddresses import geocode
import sys
import json
import time

def main():
    d = json.load(open(sys.argv[1]))
    out = open(sys.argv[2],'w')
    extra = sys.argv[3]
    for i,row in enumerate(d):
      row.update(geocode(row['address'] + extra))
      time.sleep(.1)
      if i == 0:
          break
    json.dump(d, out)
    
if __name__ == "__main__":
    main()
