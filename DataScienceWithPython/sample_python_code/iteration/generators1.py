# list comprehensions and generator expressions look very similar in their syntax, except for the use of parentheses () in generator expressions and brackets [] in list comprehensions.
# generator provides the benefit of lazy evaluation


# List of strings
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# List comprehension
fellow1 = [member for member in fellowship if len(member) >= 7]

# Generator expression
fellow2 = (member for member in fellowship if len(member) >= 7)

print(fellow1)
print(fellow2)