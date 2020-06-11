import obo
import pandas as pd
#from stemming.porter2 import stem
import csv
import nltk as nltk
from nltk.stem import WordNetLemmatizer

#stemmer = PorterStemmer()
#stemmer.stem('identified')

lemmatizer = WordNetLemmatizer()

fullwordstring =""

ipic_comments_2015 = pd.read_csv('2015-1.csv', index_col = 0)
ipic_comments_2016 = pd.read_csv('2016-1.csv', index_col = 0)
#print(str(ipic_comments))

# Iterate over rows of 2015 ipic comments
for lab, row in ipic_comments_2015.iterrows() :
	if(str(row['IPIC Comment']) == 'nan'):
		pass
	else:
		fullwordstring+= str(row['IPIC Comment'])+ " "

# Iterate over rows of 2016 ipic comments
for lab, row in ipic_comments_2016.iterrows() :
	if(str(row['IPIC Comment']) == 'nan'):
		pass
	else:
		fullwordstring+= str(row['IPIC Comment'])+ " "

lower_fullwordstring = fullwordstring.lower()
		
tokens = obo.myTokenizer(nltk.word_tokenize(lower_fullwordstring))

keyword_tokens = obo.removeMyStopTokens(tokens, obo.myStopTokens)
fulltext = nltk.Text(keyword_tokens)

print(fulltext)

fdist1 = nltk.FreqDist(fulltext)
print(fdist1)	
print ("most common 100 words")
words_dist= fdist1.most_common(100)
for word_dist in words_dist:
	print(word_dist)
	print('\n')
	
#print(type(fdist1.most_common(1000)))
#fdist1.plot(50, cumulative=True)
print("-----------------------------------")
print("hapaxes")
print(fdist1.hapaxes())
	
		
# #documents = [[stem(word) for word in sentence.split(" ")] for sentence in documents]
    
# print("String\n" + fullwordstring +"\n")

# fullwordlist = fullwordstring.split()

# wordlist = obo.removeStopwords(fullwordlist, obo.stopwords)

# final_wordlist =[]
# for word in wordlist:
	# #final_wordlist.append(stemmer.stem(word))
	# final_wordlist.append(stem(word))

	
	

# wordfreq = {}
# for w in final_wordlist:
    # #wordfreq.append(wordlist.count(w))
	# wordfreq[w]=final_wordlist.count(w)

# # print("String\n" + fullwordstring +"\n")
# # print("List\n" + str(wordlist) + "\n")
# #print("Frequencies\n" + str(wordfreq) + "\n")
# #print(str(type(zip(wordlist, wordfreq))))
# #print("Pairs\n" + str(zip(wordlist, wordfreq)))
# print(str(wordfreq))


# # with open('word_count.csv','w') as f:
    # # w = csv.writer(f)
    # # w.writerows(wordfreq.items())

# file = open("word_count1.csv","w") 
 
# #file.write("Hello World") 
# #file.write("This is our new text file") 
# #file.write("and this is another line.") 
# #file.write("Why? Because we can.") 
 
# #print (str(file))
# #file.close()	

	
# for key, value in wordfreq.items() :
    # file.write(str(key)+","+str(value)+"\n")
	
# file.close()