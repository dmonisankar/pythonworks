
def sentence_maker(phrase):
    interogatives = ("How", "Why", "What", "When", "Where")
    capitalized_phrase = phrase.capitalize()
    if capitalized_phrase.startswith(interogatives):
        return "{}?".format(capitalized_phrase)
    else:
        return "{}.".format(capitalized_phrase)

user_input_list = []

while True :
    user_input = input("say something:")
    if user_input == '\end':
        break
    else :
        user_input_list.append(sentence_maker(user_input))
        continue

print(" ".join(user_input_list))
