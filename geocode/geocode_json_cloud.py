'''Takes the json file on arg[1], which hopefully has an 'address' column, geocodes it, writes out to arg[2]'''

from __ import geocode
import json
import cloud

def main():
    cloud.setkey(1816, '3ea85e4bd2342a42db5d82896290bb73242e199b')
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
