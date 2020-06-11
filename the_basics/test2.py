def mean(value):
    #if type(value) == dict :  # this is also another way of checking
    if isinstance(value, dict):
        the_mean = sum(value.values())/len(value)
        print("inside if")
    else:
        print("inside else")
        the_mean = sum(value)/ len(value)

    return the_mean

student_marks = {"joy": 80, "raghu": 75, "sita": 90 }
print(mean(student_marks))
print(mean([23,34,36]))
