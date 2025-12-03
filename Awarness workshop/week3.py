"""
def welcome():
    print("\nWelcome to a system where area of rectangle is calculated \nother calculation coming soon..\n")

def area_rectangle(length, breadth):
    areaOfRectangle = length * breadth
    print("The length of rectangle is: ", length)
    print("The breadth of rectangle is: ", breadth)
    return areaOfRectangle 

def welcome1():
    print("\nWelcome to a system where area of Square is calculated \nother calculation coming soon..\n")

welcome1()

result = area_rectangle(10, 20)
print("The area of rectangle is: ", result)

## square 
def area_square(length, breadth):
    area_of_square = length * length 
    print("The value of breadth", breadth )
    return area_of_square

welcome()
print("The area of square is:", area_square(breadth=50, length=10))

## checkung tge scioe of a function 
def rectangle1():
    l = 10
    b = 20
    area = l * b
    print(' area in rectangle1 =', area)

def rectangle2():
    l = 5
    b = 5
    area = l * b
    print('area in rectangle2 before call to rectangle1 =', area)
    rectangle1()
    print('area in rectangle2 after call to rectangle1 = ', area)

rectangle2()
"""
maxm = 100 # global variable 
def func1(count):
    count = count + maxm 
    print("The value of count at function 1:", count)

def func2(count):
    count= count + maxm 
    print("The value of count at fucntion2", count)

func1(100)
func2(200)

# practice questions 
# write a program to check the divisibility of a number by 7 that is passed as a parameter to the user defined function. 

# Write a program that implements a user defined function that cacepts Principal, Time and rate to calculate the simple interest. (interest = P*T*R/100)
# create a function that prompts the user for two integer values and displaus the results of the first number divided by the second to two decimal places 