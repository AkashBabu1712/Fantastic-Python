"""
Python’s memory allocation and de-allocation method is automatic. The user does not have to preallocate or deallocate memory similar to using dynamic memory allocation in languages such as C or C++.

Python uses two strategies for memory allocation:
Reference counting
Garbage collection

Reference counting -
A memory management approach, to automatically manage memory by tracking how many times an object is referenced. A reference count, or the number of references that point to an object, is a property of each object in the Python language. When an object’s reference count reaches zero, it becomes un-referencable and its memory can be freed up.
"""

# Create an object
x = [1, 2, 3]

# Increment reference count
y = x

# Decrement reference count
y = None

# Create two objects that refer to each other
x = [1, 2, 3]
y = [4, 5, 6]
x.append(y)
y.append(x)

import sys

# Create an object
x = [1, 2, 3, 7, 9, 'Akash']

# Get reference count
ref_count = sys.getrefcount(x)

print("Reference count of x:", ref_count)

"""
Garbage collection - 
Garbage collection is a memory management technique used in programming languages to automatically reclaim memory that is no longer accessible or in use by the application. It helps prevent memory leaks, optimize memory usage, and ensure efficient memory allocation for the program.

Automatic Garbage Collection of Cycles -
Because reference cycles take computational work to discover, garbage collection must be a scheduled activity. Python schedules garbage collection based upon a threshold of object allocations and object de-allocations. 

When the number of allocations minus the number of de-allocations is greater than the threshold number, the garbage collector is run. One can inspect the threshold for new objects (objects in Python known as generation 0 objects) by importing the gc module and asking for garbage collection thresholds.

"""

# loading gc
import gc

# get the current collection
# thresholds as a tuple
print("Garbage collection thresholds:",
      gc.get_threshold())

# Returns the number of
# objects it has collected
# and deallocated
collected = gc.collect()

# Prints Garbage collector
# as 0 object
print("Garbage collector: collected",
      "%d objects." % collected)

i = 0


# create a cycle and on each iteration x as a dictionary
# assigned to 1
def create_cycle():
    x = {}
    x[i + 1] = x
    print(x)


# lists are cleared whenever a full collection or
# collection of the highest generation (2) is run
collected = gc.collect()  # or gc.collect(2)
print("Garbage collector: collected %d objects." % collected)

print("Creating cycles...")
for i in range(10):
    create_cycle()

collected = gc.collect()

print("Garbage collector: collected %d objects." % collected)

"""
There are two ways for performing manual garbage collection: time-based and event-based garbage collection. 

Time-based garbage collection is simple: the garbage collector is called after a fixed time interval. 
Event-based garbage collection calls the garbage collector on event occurrence. For example, when a user exits the application or when the application enters into an idle state. 
"""
