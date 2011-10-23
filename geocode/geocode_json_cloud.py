'''Takes the json file on arg[1], which hopefully has an 'address' column, geocodes it, writes out to arg[2]'''

from __ import geocode
import json
import cloud

def main():
    cloud.setkey(#NEEDS ID, KEY)
    d = json.load(open(sys.argv[1]))
    out = open(sys.argv[2],'w')
    jids = []
    for row in d:
      cb = lambda v: row.update(v)
      jids.append(cloud.call(geocode(row), _callback = cb, _type='s1'))
    cloud.join(jids)
    json.dump(d, out)
    
if __name__ == "__main__":
    main()
