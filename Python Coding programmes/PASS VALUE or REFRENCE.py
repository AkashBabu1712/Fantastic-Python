"""
Pass by value: Copy of the actual object is passed. Changing the value of the copy of the object will not change the value of the original object.
Pass by reference: Reference to the actual object is passed. Changing the value of the new object will change the value of the original object.

"""


def call_by_value(x):
    x = x * 2
    print("in function value updated to", x)
    return


def call_by_reference(list):
    list.append("D")
    print("in function list updated to", list)
    return


my_list = ["E"]
num = 6
print("number before=", num)
call_by_value(num)
print("after function num value=", num)
print("list before", my_list)
call_by_reference(my_list)
print("after function list is ", my_list)
