import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
import watson_developer_cloud.natural_language_understanding.features.v1 as \
    features


natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2017-02-27',
    username='897e7ff9-5cfb-4ce0-a7ad-ce71cb6edbcb',
    password='pjVZiijHpJ3Q')


file = open('IPIC-31087.txt','r',encoding='utf8')
txt_input =file.read()
file.close()


response_default = natural_language_understanding.analyze(
   text=txt_input,
  features=[features.Entities(), features.Relations() ])
	
response = natural_language_understanding.analyze(
   text=txt_input,
    features=[features.Entities(model='10:33c308c3-14fb-4612-a6bf-ea4da686896a'), features.Relations(model='10:33c308c3-14fb-4612-a6bf-ea4da686896a') ])

print ( 'Default NLU output')
print(json.dumps(response_default, indent=2))
print ('--------------------------------------------------------------')
print ( 'NLU output when invoked with custome wks model')
print(json.dumps(response, indent=2))


# collective_annotations = {}

# collective_annotations["relations"] = response_default["relations"] + response["relations"]
# collective_annotations["entities"] = response_default["entities"] + response["entities"]


# print(json.dumps(collective_annotations, indent=2))