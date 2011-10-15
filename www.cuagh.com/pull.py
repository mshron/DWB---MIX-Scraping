import json
import sys
import requests
import re
import csv

host = 'http://www.cuagh.com/credit-unions/credit-unions-in-ghana/'
areas = [ 'ashanti',
          'brong-ahafo',
          'central',
          'eastern',
          'greater-accra',
          'northern',
          'tema',
          'upper-east',
          'upper-west',
          'volta',
          'western',
         ]

output = dict()

outwriter = csv.writer(open('data.csv', 'wb'), delimiter=',',
                       quotechar='"', quoting=csv.QUOTE_MINIMAL)




def pull_one_area(area):
    r = requests.get(host + area)
    #print(r.content)
    soup = BeautifulSoup(r.content)
    #print(soup.prettify())
    ourdata = soup('tr')
    for d in ourdata:
        #print ("'... " + str(d) + "...'")
        ret = re.findall("<td>(.*)</td>", str(d))
        if ret:
            #print("ret: " + str(ret))
            #print("lenret: " + str(len(ret)))
            if len(ret) != 3:
                # ended
                break
            else:
                retname = ret[0]
                rettype = ret[1]
                retyear = ret[2]
                output[area]['name'] = retname
                output[area]['type'] = rettype
                output[area]['year'] = retyear
                quoted_retname = '"' + retname + '"'
                outwriter.writerow([area,quoted_retname,rettype,retyear])
    #print(ourdata[0])


from BeautifulSoup import BeautifulSoup
for area in areas:
    output[area] = dict()
    pull_one_area(area)
