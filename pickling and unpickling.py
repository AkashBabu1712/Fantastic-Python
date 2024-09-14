"""
Pickling is the process through which a Python object hierarchy is converted into a byte stream. To serialize an object hierarchy, you simply call the dumps() function.

Unpickling is the inverse operation. A byte stream from a binary file or bytes-like object is converted back into an object hierarchy. To de-serialize a data stream, you call the loads() function.

Pickling and unpickling are alternatively known as serialization.

What can be pickled and un-pickled?
In Python, the following types can be pickled −
    1. None, True, and False.
    2. integers, floating-point numbers, complex numbers.
    3. strings, bytes, bytearrays.
    4. tuples, lists, sets, and dictionaries containing only pickle objects.
    5. functions, built-in and user-defined.

Pickle Module Functions -
-----------------------------
    pickle.dump() − Write the pickled representation of the object to the open file object file.

    pickle.dumps() − Return the pickled representation of the object as a bytes object, instead of writing it to a file.

    pickle.load() − Read the pickled representation of an object from the open file object file.

    pickle.loads() − Return the reconstituted object hierarchy of the pickled representation data of an object

"""

import pickle

#input data
my_data = {'BMW', 'Audi', 'Toyota', 'Benz'}

#pickle the data
with open("demo.pickle", "wb") as file_handle:
    pickle.dump(my_data, file_handle, pickle.HIGHEST_PROTOCOL)

#Unpickle the previous data
with open("demo.pickle", "rb") as file_handle:
    res = pickle.load(file_handle)
    print(res)
