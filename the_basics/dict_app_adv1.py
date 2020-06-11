import json
from difflib import get_close_matches

my_dictionary = json.load(open('C:/Moni/PythonWorks/handson/dictionary_app/data.json'))

data = {}

for item in my_dictionary.items():
    data[item[0].lower()] = item[1]
    

def get_word_meaning(word):
    word = word.lower()
    if word in data:
        return (data[word])
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(word, data.keys())[0])
        if yn == "Y" or yn =="y" :
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N" or yn =="n" :
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."

user_input = input("enter the word:")

meaning = get_word_meaning(user_input)

if type(meaning) == list:
    for item in meaning:
        print(item)
else:
    print(meaning)

# try:
#    meaning = get_word_meaning(user_input)
#    print(meaning)
# except:
#    print("please retry with another word")
