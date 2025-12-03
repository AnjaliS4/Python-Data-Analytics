"""
f = open('firstfile.txt','r')
print(f.read())
f.close()

print("\nusing with open()")
with open(r'file_handeling.txt', 'r')as file:
    for line in file:
        print(line)

# open / with open difference: 

with open automatically closes the file after completing the operations
open() requires u to manually close the file 
with open() is considered a safer and more convenient way to handle file operations and 
also doesnt require for close() to written 

# Append
with open('file_handeling.txt', 'a') as file:
    file.write("\nHow are you today?")

# Read and print
with open('file_handeling.txt', 'r') as file:
    print(file.read())

file = open('file_handeling.txt', 'a')
file.write("\nHow are you today?")
file.close()
"""

"""
## STRING PROCESSING 
Name = "Anjali"
Age = 20
Session = "Fall2"
print(len(Name))
print(str(Age))
print(chr(68))
print (ord('5'))

# converting ascii value to characyer using chr( 
char = chr(65)
print(char)

# reversing strings
str = 'Hello, World!'
reversed_str = str[::-1]
print(reversed_str)








Notes: 
| Task                             | Function |
| -------------------------------- | -------- |
| Convert character → ASCII number | `ord()`  |
| Convert ASCII number → character | `chr()`  |

"""

## STRINGS IN PYTHON 
string.upper()
string.lower()
string.capitalize()
string.title()
string.strip()
string.split()
string.replace()
string.find()
string.startswith()
string.endswith()
