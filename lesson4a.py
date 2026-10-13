# Python functions
# A function is a block of code that performs a given task.
# We have two main types of functions i.e:
# 1. User defined functions -> They are created by the user.
# 2. in-built function -> They come with the installation of the python interpreter. e.g print(), pop(), reverse(), sort() etc.


"""
1. User defined function. To create a user defined function, we use the def keyword followed by the name of the function, parenthensis and at the end of the function defination there is a full colon. The lines that comes next are indented and they mark the body of the function.

To invoke/call the function, you do so outside of the function body by the use of the function name.
"""

def greeting():
    print("Hello there, how are you doing?")


greeting()

# example 2
print("========================")
# Below is a function that does some addition
def addition():
    number1 = 12
    number2 = 13
    number3 = 20
    sum = number1 + number2 + number3
    print("The sum of the numbers is: ", sum)


addition()
print("========================")

for greet in range(1, 6):
    greeting(), print(greet)

print("========================")
# Below is a function that demonstrates how one pick details from the user on the keyboard.

def multiplication():
    number1 = int(input("Enter the firt number: "))
    number2 = int(input("Enter the second number: "))
    product = number1 * number2
    print("The product of the two numbers is: ", product)
    print("----------")


# for x in range(3):
#     multiplication()

print("========================")
# Create a function that is able to calculate the simple interest gained after a person inversted 75000 for 5 years and the rate was 6.5%. Formulae = si = (principal * rate * time) /100

def simple_interest():
    investment = 75000
    time = 5
    rate = 6.5
    interest = (investment * rate * time) / 100
    print("The interest gained is: ", interest)

simple_interest()