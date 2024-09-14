"""
if you want to copy object, the assignment operator won’t fulfil the purpose. It creates bindings between a target and an object i.e., it never creates a new object. It only creates a new variable sharing the reference of the original object. To fix this, the copy module is provided. This module has generic shallow and deep copy operations.

Shallow Copy
A shallow copy constructs a new compound object and then inserts references into it to the objects found in the original. It uses the following method to copy objects  −
    copy.copy(x)
    Return a shallow copy of x.

Deep Copy
A deep copy constructs a new compound object and then, recursively, inserts copies into it of the objects found in the original. It uses the following method to copy objects  −

    copy.deepcopy(x[, memo])
    Return a deep copy of x. Here, memo is a dictionary of objects already copied during the current copying pass;


"""

import copy

# Create a List
myList = [[5, 10], [15, 20]]

# Display the list
print("List = ", myList)

# Shallow Copy
myList2 = copy.copy(myList)

# Display the copy of the List
print("Shallow copy of the list =", myList2)

# Deep Copy
myList1 = copy.deepcopy(myList)

# Display the copy of the List
print("Deep copy of the list =", myList1)
