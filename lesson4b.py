# Functions with parameters. 
# Parameters are values that get passed as arguments when invoking a function.

def greeting(name):
    print("Hello", name, "How have you been?")

greeting("John")
greeting("Mary")
greeting("Joseph")

print("===================")

def message(name):
    print("Greeting, ", name, " You are kindly reminded to attend the general meeting to be held on 16th October 2026.")


message("Benard Kamotho")
message("Linet Wambui")
message("Christina Maabinyana")

print("===================")

def addition(number1, number2, number3):
    sum = number1 + number2 + number3
    print("The sum of the numbers is: ", sum)

addition(10, 20, 5)

print("===================")
# Create a function that accepts parameters that is able to calculate the simple interest gained after a person inversted 75000 for 5 years and the rate was 6.5%. Formulae = si = (principal * rate * time) /100

def simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    print("The interest Gained is: ", interest)

simple_interest(75000, 6.5, 5)
simple_interest(45000, 7, 4)

print("===================")
# Create a function that accepts parameters to calculate the body mass index of a person whose weight is 55kg and height is 1.75 meters. formulae BMI = weight / (height * height)
