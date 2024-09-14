"""
Negative Indexing is used to in Python to begin slicing from the end of the string i.e. the last. Slicing in Python gets a sub-string from a string. The slicing range is set as parameters i.e. start, stop, and step.

slicing from index start to index stop-1
arr[start:stop]

slicing from index start to the end
arr[start:]

slicing from the beginning to index stop - 1
arr[:stop]

slicing from the index start to index stop, by skipping step
arr[start:stop:step]

"""

# Create a String
myStr = 'This is very cool!'

# Display the String
print("String = ", myStr)

# Slice the string
# Negative Indexing
print("String after slicing (negative indexing) = ", myStr[-4:-1])

#Slice the string
# Negative Indexing with step
print("String after slicing (negative indexing) = ", myStr[-9:-3:2])

# Reverse Slice
print("Reverse order of the String = ", myStr[::-1])

