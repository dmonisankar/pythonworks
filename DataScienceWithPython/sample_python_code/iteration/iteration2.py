# Create an iterator for range(3): small_value
small_value = iter(range(3))

# Print the values in small_value
print(next(small_value))
print(next(small_value))
print(next(small_value))

# Loop over range(3) and print the values
for i in range(3):
    print(i)


# Create an iterator for range(10 ** 100): googol
googol = iter(range(10 ** 100))


# range() doesn't actually create the list; instead, it creates a range object with an iterator that produces the values until it reaches the limit (in the example, until the value 4). If range() created the actual list, calling it with a value of 10100 may not work, especially since a number as big as that may go over a regular computer's memory. The value 10100 is actually what's called a Googol which is a 1 followed by a hundred 0s. That's a huge number!

# Print the first 5 values from googol
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))
