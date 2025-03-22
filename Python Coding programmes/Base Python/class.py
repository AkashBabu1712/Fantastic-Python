# Python class and objects
'''Python is an object-oriented programming language, which means it allows you to define classes and create
objects(instances of classes). A class is a blueprint for creating objects, providing initial values for state(member variables or attributes) and implementations of behavior(member functions or methods).'''


# define a class
class Bike:
    name = ""
    gear = 0

# create object of class
bike1 = Bike()

# access attributes and assign new values
bike1.gear = 11
bike1.name = "Mountain Bike"

print(f"Name: {bike1.name}, Gears: {bike1.gear} ")

#######################################################

# create a class
class Room:
    length = 0.0
    breadth = 0.0
    
    # method to calculate area
    def calculate_area(self):
        print("Area of Room =", self.length * self.breadth)

# create object of Room class
study_room = Room()

# assign values to all the properties 
study_room.length = 42.5
study_room.breadth = 30.8

# access method inside class
study_room.calculate_area()
