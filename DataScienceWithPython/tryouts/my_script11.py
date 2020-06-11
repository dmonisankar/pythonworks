import json
import sys


dic_a ={'entities': ['person','organization'],
		'relations':['employedBy']}
		
		
#print(json.dumps(dic_a, indent=2))	

dic_b ={'entities': ['person','facilities'],
		'relations':['foundedBy']}	
		
dic_collection={}

dic_collection['entities']= dic_a['entities'] + dic_b['entities']
dic_collection['relations'] = dic_a['relations']+dic_b['relations']
		
#dic_a.update(dic_b);


print(json.dumps(dic_collection, indent=2))	