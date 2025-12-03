
import math 
i = 2  
"""while i <= 5:  
    print(f"\nMultiplication Table for {i}:")
    j = 1       
    while j <= 10:  
        print(f"{i} x {j} = {i * j}")
        j = j + 1
    i = i + 1


a = 2
#n = 10
while a <= 5:

    b = 1
    while b <= 10:
        print("the multiplication from 2 to 5 is:",  f"{a * b}")
        b = b + 1
    a = a + 1

num = 25 
while(num>=10):
    print("THe square root of", num, "is", math.sqrt(num))
    num -= 5



### UPLOAD THIS IS GITHUB AS INDIVIDUAL PROJECTS 
radius = float(input("enter the radius of the circle"))
circumference =  2 * radius * math.pi
print(f"The circumference of the circle is {circumference:.2f}")
i
# 1. write a python program to claculate BMI of a person when all 
# pareameters are provided BMI = weight(kg)/height(m^2)
weight = float(input("enter your weight here in kg: "))
height = float(input ("enter your height here in meter: ")) # mine is 1.8 
BMI = float (weight/height ** 2)
print(f"your BMI is:, {BMI}")


# 2. write a program to find the cube root of a number. 
# Promt the user to input a number and print the cube root of the number 


# 3. suppose u ar ea teacher and u want to create a program that takes in grades from three 
# exams and calculates the average grade for a student. Develop a program to print out the average marks of particular student. 


# LOOP QUESTIONS 
# number 1: write a while loop to reverse a given number input: 4567. output: 7654 



# Take input from the user and convert to integer
length = int(input("Enter the length of the rectangle: "))
breadth = int(input("Enter the breadth of the rectangle: "))

# Define the function to calculate the area
def area_rectangle(length, breadth):
    area = length * breadth  # Calculate the area
    return area

# Call the function with the arguments and print the result
print("The area of the rectangle is: ", area_rectangle(length, breadth))

"""

