"""
A generator function in Python is defined like a normal function, but whenever it needs to generate a value, it does so with the yield keyword rather than return. If the body of a def contains yield, the function automatically becomes a Python generator function.

def function_name():
    yield statement


Generator Object
Python Generator functions return a generator object that is iterable, i.e., can be used as an Iterator. Generator objects are used either by calling the next method of the generator object or using the generator object in a “for in” loop.


"""


#Python Class Iterator Implementation
class get_odds:
    def __init__(self, max):
        self.n = 3
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        if self.n <= self.max:
            result = self.n
            self.n += 2
            return result
        else:
            raise StopIteration


numbers = get_odds(10)
print(next(numbers))
print(next(numbers))
print(next(numbers))


#Python Generator Implementation
def get_odds_generator():
    n = 1

    n += 2
    yield n

    n += 2
    yield n

    n += 2
    yield n

print('--')

numbers = get_odds_generator()
print(next(numbers))
print(next(numbers))
print(next(numbers))


