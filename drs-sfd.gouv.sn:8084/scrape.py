'''Pulls data from the Sengegalese Cartographic Service for MIX'''

import BeautifulSoup
import requests
import re
import json

def get_departments(url):
    _d = requests.get(url)
    d = BeautifulSoup.BeautifulSoup(_d)
    return d.findAll('form')[1].findAll('option')[1:] #assumes it's the middle one

def each_page(row):
    value = row.attrs['value']

        
