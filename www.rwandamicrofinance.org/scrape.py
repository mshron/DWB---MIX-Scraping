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

def eachpage(url):
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
        out['type'] = 'MFI'
        result.append(out)
        
    n = d.findAll('a', attrs={'title':'Next'})
    try:
        n = n[0].attrs[1][1]
    except:
        n = None
    return result,n

def main():
    start = 'index.php?option=com_sobi2&catid=7&Itemid=94&lang=en'
    outfile = open('rwandamicrofinance.json','w')
    out = []
    result, n = eachpage(start)
    out.extend(result)
    while n!=None:
        result,n = eachpage(n)
        out.extend(result)
    json.dump(out, outfile)

if __name__ == "__main__":
    main()
