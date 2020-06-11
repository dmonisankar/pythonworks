
# This program looks for *.docx file in current folder and generate json file in the json format defined KLM Cargo Rules.
# This also generates a text file with the docx content
# in the current folder there must a RuleContext.txt from where it takes the value of json element RuleContext
# Currently RuleSource and RuleAttribute jsonelements are hardcoded.



import docx
import sys
import json
import os

for file in os.listdir():
	if file.endswith(".docx"):
		print(file)

try:
	
	for filename in os.listdir():
		if filename.endswith(".docx"):
			print(filename)
			#docname = sys.argv[1]
			#print(docname)
			doc = docx.Document(filename)
			
			with open('RuleContext.txt', mode='r') as confile:
				context_str=confile.read()
			
			textfilename = filename.split(".")[0] + '.txt'
			jsonfilename = filename.split(".")[0] + '.json'
			
			fullText = []
			
			
			with open(textfilename, mode='wt', encoding='utf-8') as file:
				for para in doc.paragraphs:
					file.write(para.text)
					file.write('\n')
					fullText.append(para.text)
			
			strtext= '\n'.join(fullText)
			print(context_str)
			print(strtext)
			
			
			data = {}
			data['RuleSource'] = 'Lithium Battery Shipping Guidelines - 4th Edition'
			data['RuleContext']= context_str
			data['RuleName']= filename.split(".")[0]
			data['RuleAttributes']={"sp_handling_instr": "XXX", "additional_attr":"xxx"}
			data['Rule']= strtext
			
			with open(jsonfilename, mode='wt', encoding='utf-8') as jfile:
				json.dump(data, jfile)
			
	
	
except ValueError:
	print('please enter a valid docx file')