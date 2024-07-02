"""
Break -> The break statement terminates the loop immediately and the control flows to the statement after the body of the loop.

Continue -> The continue statement terminates the current iteration of the statement, skips the rest of the code in the current iteration and the control flows to the next iteration of the loop.

Pass -> As explained above, the pass keyword in Python is generally used to fill up empty blocks and is similar to an empty statement represented by a semicolon in languages such as Java, C++, Javascript, etc.

"""

# Python program to demonstrate
# break statement

s = 'Woods_are_lovely_dark_and_deep'
# Using for loop
for letter in s:

    print(letter)
    # break the loop as soon it sees 'e'
    # or 's'
    if letter == 'e' or letter == 's':
        break

print("Out of for loop")
print()

i = 0

# Using while loop
while True:
    print(s[i])

    # break the loop as soon it sees 'e'
    # or 's'
    if s[i] == 'e' or s[i] == 's':
        break
    i += 1

print("Out of while loop")
