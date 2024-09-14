"""
To pass unspecified number of arguments to a function usually *args and **kwargs properties are used. The *args property is used to send a non-keyword variable length argument to a function call whereas **kwargs keyword is used to pass a keyword length of arguments to a function.

Keyword arguments (or arguments) are the values that is preceded by an identifier “=” in a function call for e.g. “name=”.

The primary benefits of using *args and **kwargs are readability and convenience, but they should be used with care.

Note − It is not necessarily required to write *args and **kwargs. There is only a need for the asterisk (*). For instance, you could write *var and **vars as well.

"""


#*args

def multiply(*args):
    print(args, type(args))


multiply(6, 78)


def multiply(*args):
    x = 1
    for i in args:
        x = x * i
    print('The product of the numbers is:', x)


multiply(5, 87)
multiply(8, 11)
multiply(6, 9, 4, 7)
multiply(2, 11, 98)


#*kwargs

def gadgets_price(**kwargs):
    print(kwargs, type(kwargs))


gadgets_price(laptop=60000, smartphone=10000, earphones=500)


def gadgets_price(**items):
    total = 0
    for price in items.values():
        total += price
    return total


print('The net amount of the gadgets is:', (gadgets_price(laptop=60000, smartphone=10000, earphones=500)))
print('The net amount of the gadgets is:', (gadgets_price(laptop=60000, smartphone=10000, desktop=45768)))
print('The net amount of the gadgets is:', (gadgets_price(laptop=60000, TV=85965)))
