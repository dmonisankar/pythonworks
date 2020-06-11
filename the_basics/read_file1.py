# myfile = open("C:/Moni/PythonWorks/the_basics/fruits.txt")
# content = myfile.read()
# myfile.close()
# print(content[:10])

def str_count(character, filepath):
    # myfile = open(filepath)
    # content = myfile.read()
    # myfile.close()

    with open(filepath) as myfile :
        content = myfile.read()

    return content.count(character)


filepath = "C:/Moni/PythonWorks/the_basics/fruits.txt"
character = 'a'

print(str_count(character, filepath))
