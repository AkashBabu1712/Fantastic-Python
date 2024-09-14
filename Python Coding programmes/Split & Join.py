"""
In Python, we can use the function split() to split a string and join() to join a string. the split() method in Python split a string into a list of strings after breaking the given string by the specified separator.
Python String join() method is a string method and returns a string in which the elements of the sequence have been joined by the str separator.

Time complexity: O(n), where n is the length of given string
Auxiliary space: O(n)
"""

# input string
s = 'Lets consider yourself'
# print the string after split method
print(s.split(" "))
# print the string after join method
print("-".join(s.split()))


