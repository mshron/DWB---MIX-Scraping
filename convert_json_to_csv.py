#!/usr/bin/env python
'''Does what the title says. %{progname} jsonfile csvoutfile'''

import json
import csv
import sys

def main():
    infile = sys.argv[1]
    outfile = sys.argv[2]
    jdata = json.load(open(infile))
    cols = set()
    for item in jdata:
        cols.update(set(item.keys()))
    csvout = csv.writer(open(outfile,'w')) 
    csvout.writerow(list(cols)) 
    for row in jdata:
        d = [row.get(c,'').encode('utf-8') for c in cols]
        csvout.writerow(d)
    return

if __name__ == "__main__":
    main()
