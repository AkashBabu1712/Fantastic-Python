"""
The range() method in Python is used to return a sequence object. It is used in Python 3.x
The xrange() is used to generate sequence of number and used in Python 2.x. Therefore, there’s no xrange() in Python 3.x.

range(start, stop, step)
        start − Integer specifying at which position to start.
        stop − Integer specifying at which position to stop.
        step − Integer specifying increment i.e. skip step
"""

#Range
a = range(2, 8)
for n in a:
    print(n)

print('With steps Parameters')

# Defined start, stop and step parameters
a = range(2, 10, 3)
for n in a:
    print(n)

