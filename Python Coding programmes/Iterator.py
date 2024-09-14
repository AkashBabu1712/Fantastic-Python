"""
What are iterators in Python?

 - An iterator is an object.
 - It remembers its state i.e., where it is during iteration (see code below to see how)
 - __iter__() method initializes an iterator.
 - It has a __next__() method which returns the next item in iteration and points to the next element. Upon reaching the end of iterable object __next__() must return StopIteration exception.
 - It is also self-iterable.
 - Iterators are objects with which we can iterate over iterable objects like lists, strings, etc.

"""


# An iterable user defined type
class Test:

    # Constructor
    def __init__(self, limit):
        self.limit = limit

    # Creates iterator object
    # Called when iteration is initialized
    def __iter__(self):
        self.x = 10
        return self

    # To move to next element. In Python,
    # we should replace next with __next__
    def __next__(self):
        # Store current value of x
        x = self.x

        # Stop iteration if limit is reached
        if x > self.limit:
            raise StopIteration

        # Else increment and return old value
        self.x = x + 1
        return x


# Prints numbers from 10 to 15
for i in Test(15):
    print('The numbers are as : ', i)

# Prints nothing
for i in Test(5):
    print('The number is nothing: ', i)
