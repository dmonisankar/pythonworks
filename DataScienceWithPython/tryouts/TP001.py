import obo
import pandas as pd
from stemming.porter2 import stem
import csv
#from nltk.stem.porter import *

#stemmer = PorterStemmer()

#stemmer.stem('identified')





fullwordstring =""

# fullwordstring = 'Container was found malfunctioning and analysis of the data logger confirm that reefer was most likely leaking refrigerant and consequently loosing cooling capacity. Cargo was found in apparent sound condition, hence no claim expected. '
# fullwordstring += 'Cause of loss ripes leading to the consignment being a total loss. According to the surveyors report there were a number of factors giving rise to the condition of the fruit:'

ipic_comments = pd.read_csv('sample-text11.csv', index_col = 0)
#print(str(ipic_comments))



# Iterate over rows of ipic comments
for lab, row in ipic_comments.iterrows() :
	if(str(row['IPIC Comment']) == 'nan'):
		pass
	else:
		fullwordstring+= str(row['IPIC Comment'])+ " "

		
#documents = [[stem(word) for word in sentence.split(" ")] for sentence in documents]
    
print("String\n" + fullwordstring +"\n")

fullwordlist = fullwordstring.split()

wordlist = obo.removeStopwords(fullwordlist, obo.stopwords)

final_wordlist =[]
for word in wordlist:
	#final_wordlist.append(stemmer.stem(word))
	final_wordlist.append(stem(word))

	
	

wordfreq = {}
for w in final_wordlist:
    #wordfreq.append(wordlist.count(w))
	wordfreq[w]=final_wordlist.count(w)

# print("String\n" + fullwordstring +"\n")
# print("List\n" + str(wordlist) + "\n")
#print("Frequencies\n" + str(wordfreq) + "\n")
#print(str(type(zip(wordlist, wordfreq))))
#print("Pairs\n" + str(zip(wordlist, wordfreq)))
print(str(wordfreq))


# with open('word_count.csv','w') as f:
    # w = csv.writer(f)
    # w.writerows(wordfreq.items())

file = open("word_count1.csv","w") 
 
#file.write("Hello World") 
#file.write("This is our new text file") 
#file.write("and this is another line.") 
#file.write("Why? Because we can.") 
 
#print (str(file))
#file.close()	

	
for key, value in wordfreq.items() :
    file.write(str(key)+","+str(value)+"\n")
	
file.close()