'''Takes the json file on arg[1], which hopefully has an 'address' column, geocodes it, writes out to arg[2]'''

from geocodeAddresses import geocode
import json
import time

def main():
    d = json.load(open(sys.argv[1]))
    out = open(sys.argv[2],'w')
    for row in d:
      row.update(geocode(row))
      time.sleep(.1)
    json.dump(d, out)
    
if __name__ == "__main__":
    main()
