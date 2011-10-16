'''Code to scrape microfinance data from http://www.ncr.org.za/register_of_registrants/index.php'''

import BeautifulSoup as bs
import requests
import re
import json
import pickle

def scrape_raw(url, registrant_type):
	post_args = {"ns_BType": registrant_type, "ns_SearchText": "*", "ns_Town": "All", "_submit_check_": 1, "ns_cancel": "registered"}
	__d = requests.post(url, data=post_args)
	_d = __d.content
	
	#output = open('data.pkl', 'wb')
	#pickle.dump(_d, output)
	#output.close()
	
	#pkl_file = open('data.pkl', 'rb')
	#_d = pickle.load(pkl_file)
	#pkl_file.close()
	
	d = bs.BeautifulSoup(_d)
	return d.findAll(['table'], attrs={'width': 740})
	
def parse_tables(tables, registrant_type):
	out = []
	reg_types = dict({'DC':'Debt Counsellors', 'CP1': 'Credit Providers - Head Quarters', 'CB1':'Credit Bureaus'})
	for t in tables:
		record = {}
		_address = t.findAll('span',attrs={'class':'Text2'})
		#skip tables without data (the first and last are used for formatting the page)
		if len(_address) == 3:
			record['name'] = t.find('span').text
			record['address'] =_address[0].text
			record['phone_number'] = _address[1].text
			record['registrant_type'] = reg_types[registrant_type] 
			out.append(record)  
	return out

	
def main():
	url = 'http://www.ncr.org.za/register_of_registrants/index.php'
	registrant_types = ['CB1', 'CP1', 'DC']
	result = []
	for registrant_type in registrant_types:
		d = scrape_raw(url,registrant_type)
		out = parse_tables(d, registrant_type)
		result.extend(out)
	outfile = open('ncr.json','w')
	json.dump(result,outfile)
	outfile.close()

if __name__ == "__main__":
	main()
