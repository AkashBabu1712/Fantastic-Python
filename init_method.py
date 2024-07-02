"""
Init -  is a constructor method in Python and is automatically called to allocate memory when a new object/instance
is created. All classes have a __init__ method associated with them. It helps in distinguishing methods and
attributes of a class from local variables.
"""


#Creating class Animal
class Animal:
    def __init__(self, name, species, features, categories):
        self.name = name
        self.species = species
        self.features = features
        self.categories = categories

    #Creating function Kingdom
    def kingdom(self):
        print(f"The Animal kingdom name:", self.name)
        print(f"The Animal kingdom species:", self.species)
        print(f"The Animal kingdom features:", self.features)
        print(f"The Animal kingdom categories:", self.categories)


#creating object
A1 = Animal('Human', 'Homo Sapiens', 'Walk on 2 hands', 'Mammals')

A1.kingdom()  #calling function

# Python program to
# demonstrate init with
# inheritance

# class A(object):
#     def __init__(self, something):
#         print("A init called")
#         self.something = something
#
#
# class B(A):
#     def __init__(self, something):
#         print("B init called")
#         self.something = something
#         # Calling init of parent class
#         A.__init__(self, something)
#
#
# obj = B("Something")
