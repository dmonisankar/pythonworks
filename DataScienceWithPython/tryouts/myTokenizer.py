import re as re
import nltk as nltk
import sys
import obo as myhelper

s = input("put your text here\n")
tokens = nltk.word_tokenize(s)

print(tokens)

# reg_ex_dot = '[a-zA-Z]+\.[a-zA-Z]'

# #print(type(tokens));  # print object type of variable 'tokens'

# updated_tokens =[]

# for idx, token in enumerate(tokens):
	# matchObj_dot = re.match( reg_ex_dot, token, re.I)
	# if(matchObj_dot is not None):
		# dot_pos = token.index('.')
		# sub_token1 = token[:dot_pos]
		# sub_token2 = token[(dot_pos+1):]
		# updated_tokens.append(sub_token1)
		# updated_tokens.append(sub_token2)	
	# else:
		# updated_tokens.append(token)
		
	

# print(updated_tokens);

updated_tokens = myhelper.myTokenizer(tokens)

print(updated_tokens)