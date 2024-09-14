"""
Lambda is an anonymous function in Python, that can accept any number of arguments, but can only have a single expression. It is generally used in situations requiring an anonymous function for a short time period. Lambda functions can be used in either of the two ways:

 - Assigning lambda functions to a variable
 - Wrapping lambda functions inside another function

lambda arguments : expression

"""

str1 = 'My name is Mohan'

upper = lambda string: string.upper()
print(upper(str1))


format_numeric = lambda num: f"{num:e}" if isinstance(num, int) else f"{num:,.2f}"

print("Int formatting:", format_numeric(1000000))
print("float formatting:", format_numeric(999999.789541235))


def cube(y):
    return y * y * y


lambda_cube = lambda y: y * y * y
print("Using function defined with `def` keyword, cube:", cube(5))
print("Using lambda function, cube:", lambda_cube(5))


#List Comprehension
is_even_list = [lambda arg=x: arg * 10 for x in range(1, 5)]
for item in is_even_list:
    print(item())


#If else statement
Max = lambda a, b: a if (a > b) else b
print(Max(1, 2))


#Using Map Function
animals = ['dog', 'cat', 'parrot', 'rabbit']
uppered_animals = list(map(lambda animal: animal.upper(), animals))

print(uppered_animals)
