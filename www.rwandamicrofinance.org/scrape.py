'''Follows pages on Rwanda Microfinance Web Portal'''

import BeautifulSoup
import requests
import json
import re

base = 'http://www.rwandamicrofinance.org/'

def getKind(td, label, replace=""):
    try:
        return td.findAll('span', attrs={'class':label})[0].text
    except IndexError:
        return ''

def eachpage(url, kind):
    _d = requests.get(base+url)
    d = BeautifulSoup.BeautifulSoup(_d.content)
    result = []
    for td in d.findAll('td',attrs={'style':"width: 50%; background-image: url(http://www.rwandamicrofinance.org/components/com_sobi2/images/backgrounds/green.gif);border-style: solid; border-color: #808080"}):
        out = {}
        out['name'] = td.findAll('p')[0].text
        out['place'] = getKind(td, 'sobi2Listing_field_place')
        out['email'] = getKind(td, 
            'sobi2Listing_field_email').replace('Email:','')
        out['contact_person'] = getKind(td,
            'sobi2Listing_field_contact_person').replace('Contact Person:','')
        out['phone'] = getKind(td,
            'sobi2Listing_field_phone').replace('Phone:','')
        out['type'] = kind
        result.append(out)
        
    n = d.findAll('a', attrs={'title':'Next'})
    try:
        n = n[0].attrs[1][1]
    except:
        n = None
    return result,n

def main():
    out = []
    kinds = {'7': 'MFI', '8': 'Unions', '9': 'SARL', '10': 'SA'}
    for k,v in kinds.iteritems():
        start = 'index.php?option=com_sobi2&catid=%s&Itemid=94&lang=en'%k
        outfile = open('rwandamicrofinance.json','w')
        result, n = eachpage(start, v)
        out.extend(result)
        while n!=None:
            result,n = eachpage(n, v)
            out.extend(result)
    json.dump(out, outfile)

if __name__ == "__main__":
    main()
