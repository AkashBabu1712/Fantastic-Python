"""String slicing in Python is about obtaining a sub-string from the given string by slicing it respectively from
start to end.

Python slicing can be done in two ways:
1. Using a slice() method
2. Using the array slicing  [:: ] method

"""

# Method 1: Using the slice() method
# The slice() constructor creates a slice object representing the set of indices specified by range(start, stop, step).

# Syntax:
# slice(stop)
# slice(start, stop, step)
#-> Return Type: Returns a sliced object containing elements in the given range only.

String = "Akash"

# Using slice constructor
s1 = slice(3)
s2 = slice(1, 5, 2)
s3 = slice(-1, -12, -2)

print("String slicing:")
print(String[s1])
print(String[s2])
print(String[s3])

# Method 2: Using the List/array slicing  [ :: ]  method - indexing syntax can be used as a substitute for the slice object. This is an easy and convenient way to slice a string using list slicing and Array slicing both syntax-wise and execution-wise. A start, end, and step have the same mechanism as the slice() constructor.

# arr[start:stop]         # items start through stop-1
# arr[start:]             # items start through the rest of the array
# arr[:stop]              # items from the beginning through stop-1
# arr[:]                  # a copy of the whole array
# arr[start:stop:step]    # start through not past stop, by step

# String slicing
String = "This_is_my_rule"

# Using indexing sequence
print(String[:3])  #Thi

print(String[1:5:2])  #hs

print(String[-1:-12:-2])  #eu_ms_

