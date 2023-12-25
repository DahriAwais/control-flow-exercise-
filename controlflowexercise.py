#Exercise 1:

number = int(input("enter number ::"))
if number % 2 == 0:
    print (f"{number} is even")
else:
    print(f"{number} is odd")
#Exercise 2:

year = int(input("Enter a year: "))

if year % 400 == 0:
    print(f"{year} is a leap year")
elif year % 100 == 0:
    print(f"{year} is not a leap year")
elif year % 4 == 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
#    Exercise 3:

age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")
#Exercise 4:

username = input("Enter your username: ")
password = input("Enter your password: ")

if username == "admin" and password == "12345":
    print("Login successful")
else:
    print("Login failed")
#Exercise 5:

num = float(input("Enter a number: "))

if num > 0:
    print("Positive number.")
elif num == 0:
    print("Zero.")
else:
    print("Negative number.")
#Exercise 6:

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3

print(f"The largest number is {largest}")
#Exercise 7:

score = float(input("Enter your score: "))

if score >= 90:
    print("Your grade is A.")
elif score >= 80:
    print("Your grade is B.")
elif score >= 70:
    print("Your grade is C.")
elif score >= 60:
    print("Your grade is D.")
else:
    print("Your grade is F.")
#Exercise 8:

import math

num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            print(f"{num} is not a prime number")
            break
    else:
        print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")
#Exercise 9:

if year % 400 == 0:
    print(f"{year} is a leap year")
elif year % 100 == 0:
    print(f"{year} is not a leap year")
elif year % 4 == 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
#Exercise 10:

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if num1 > num2:
    print(f"{num1} is larger than {num2}")
elif num2 > num1:
    print(f"{num2} is larger than {num1}")
else:
    print("The numbers are equal")