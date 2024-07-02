"""
Decorators in Python are essentially functions that add functionality to an existing function in Python without changing the structure of the function itself. They are represented the @decorator_name in Python and are called in a bottom-up fashion.

First Class Objects -
In Python, functions are first class objects which means that functions in Python can be used or passed as arguments.
Properties of first class functions:
A function is an instance of the Object type.
You can store the function in a variable.
You can pass the function as a parameter to another function.
You can return the function from a function.
You can store them in data structures such as hash tables, lists, …
"""

#Treat function as an object
green = [1, 4, 6, 8, 45]


def nature(green):
    for g in green:
        if g != 0:
            print(f"The nature is secure: {g}")
        else:
            print('In Danger')
    print('All elements processed')


#nature(green)

Env = nature

# print("All is Well")
Env(green)
