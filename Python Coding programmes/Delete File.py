"""
When any large program is created, usually there are small files that we need to create to store some data that is needed for the large programs. when our program is completed, so we need to delete them. In this article, we will see how to delete a file in Python.

Methods to Delete a File in Python -
    1. Python Delete File using os. remove
    2. Delete file in Python using the send2trash module
    3. Python Delete File using os.rmdir

"""

#pip install os

import os


def check_file_existence(file_path):
    if os.path.exists(file_path):
        print(f'The file "{file_path}" exists.')
    else:
        print(f'The file "{file_path}" does not exist.')


# Example usage:
file_path = 'path/to/your/file.txt'
check_file_existence(file_path)

import os

print("Enter 'quit' for exiting the program")
filename = input('Enter the name of the file, that is to be deleted : ')
if filename == 'quit':
    exit()
else:
    print('\nStarting the removal of the file !')
    os.remove(filename)

    print('\nFile, ', filename, 'The file deletion is successfully completed !!')

#OUTPUT
# Enter 'quit' for exiting the program
# Enter the name of the file, that is to be deleted : C:\Users\akash\Desktop\Notepad\Network troubleshooting commands.txt
