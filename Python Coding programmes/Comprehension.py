"""
Using comprehensions saves a lot of time and code that might be considerably more verbose (containing more lines of code).

Types of comprehensions -

List Comprehensions
Dictionary Comprehensions
Set Comprehensions
Generator Comprehensions



"""
#without using List Comprehensions
input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]
output_list = []

for var in input_list:
    if var % 2 == 0:
        output_list.append(var)

print("Output List using for loop:", output_list)

#Using List Comprehension
input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]

list_using_comp = [var for var in input_list if var % 2 == 0]

print("Output List using list comprehensions:", list_using_comp)


#Dict Comprehension
input_list = [1,2,3,4,5,6,7]

dict_using_comp = {var:var ** 3 for var in input_list if var % 2 != 0}

print("Output Dictionary using dictionary comprehensions:",dict_using_comp)

state = ['Gujarat', 'Maharashtra', 'Rajasthan']
capital = ['Gandhi nagar', 'Mumbai', 'Jaipur']

dict_using_comp = {key:value for (key, value) in zip(state, capital)}

print("Output Dictionary using dictionary comprehensions:", dict_using_comp)
