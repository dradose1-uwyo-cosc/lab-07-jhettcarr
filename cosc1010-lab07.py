# Jhett Carr
# UWYO COSC 1010
# Submission Date: 10/30/2024
# Lab 07
# Lab Section: 15
# Sources, people worked with, help given to: 
# Kaleb Moler
# Jay Trujillo
# Ireeann Anderson
# Openstax / reddit 
# Replit


# Prompt the user for an upper bound 
# Write a while loop that gives the factorial of that upper bound
# This will need to be a positive number
# For this you will need to check to ensure that the user entered a number
    # To do so you can use the methods `.isdigit()` or `.isnumeric()`
    # If a user did not enter a number output a statement saying so
# You will continue to prompt the user until a proper integer value is entered

while True:
    n = input("Please enter an upper-bound number: ")

    if n.isdigit():
        n = int(n)
        if n >= 0:
            factorial = 1
            var = n
            while var > 0:
                factorial = factorial * var
                var = var - 1
            print(f"The factorial is {factorial}")
            break 
        else:
                print("Enter a positive number")
    else:
        print("Invalid input, enter a positive number")

print("*"*75)
# Create a while loop that prompts a user for input of an integer values
# Sum all inputs. When the user enters 'exit' (regardless of casing) end the loop
# Upon ending the loop print the sum
# Your program should accept both positive and negative input
# Remember all inputs from stdin are strings, so you will need to convert the string to an int first
# Before you convert the number you need to check to ensure that it is a numeric string
    # To do so you can use the methods `.isdigit()` or `.isnumeric()`
    # This will return true if every digit in your string is a numerical character
    # However, that means a string such as `-1` would return false, even though your program should accept negative values
    # This means you will need to have a check to see if `-` is first character of the string before you check if it is numerical
    # If it is in the string you will need to remove the `-` character, and know that it will be a negative number, so a subtraction from the overall sum
    # I recommend checking out: https://www.w3schools.com/python/ref_string_replace.asp to figure out how one may remove a character from a string
# All this together means you will have an intensive while loop that includes multiple if statements, likely with some nesting 
# The sum should start at 0 

num_sum = 0
while True:
    num = input("Enter a number or 'exit' to quit: ")
    if num.lower() == "exit" :
        break
    if num.isdigit() or (num[0] == "-" and num[1:].isdigit()):
        number = int(num)
        num_sum += number
    else:
        print("Invalid input, enter a number or 'exit' to quit")

print(f"Your final sum is {num_sum}")

print("*"*75)
# Now you will be creating a two operand calculator
# It will support the following operators: +,-,/,*,% 
# So accepted input is of the form `operand operator operand` 
# You can assume that the user is competent and will only input strings of that form 
# You will again need to verify that the operands are numerical values
# For this assume only positive integers will be entered, no need look for negative numbers 
# You will need to check the string for which operator it contains
# Once you do, you will need to remove the operands from the string
# This can be done in multiple ways:
    # You can go through the string in a loop and create a substring of the characters until an operator is reached
        # Upon reaching the operator you will switch to another substring and add all characters following to the second new string 
    # Alternatively you can use the `.split()` method to split the string around an operator: https://www.w3schools.com/python/ref_string_split.asp
# Your program will need to work with whatever spacing is given  
    # So, it should function the same for `5 + 6` as `5+6`
# Print the result of the equation
# Again, loop through prompting the user for input until `exit` in any casing is input 

def calc(val_1, oper, val_2):
    if(oper == "+"):
        return(val_1 + val_2)
    elif(oper == "-"):
        return(val_1 - val_2)
    elif(oper == "*"):
        return(val_1 * val_2)
    elif(oper == "/"):
        if(val_2 != 0):
              return(val_1 / val_2)
        else:
            return("Cannot divide by zero, try again")
    elif(oper == "%"):
        return(val_1 % val_2)
    else:
        return("Invalid operation, try again")

def user_calc():
    while True:
        inp = input("Enter an equation (eg. 5+5, 10/2, etc.) using +, -, *, /, %, or 'exit' to quit: ")
        if inp.lower() == "exit" :
            break
        inp = inp.replace(" ", "")
        v1 = ""
        v2 = ""
        oper = ""
        move = False

        for char in inp:
            if char.isdigit() and not move:
                v1 += char
            elif char.isdigit() and move:
                v2 += char
            else:
                oper = char
                move = True
        if v1 and v2 and oper:
            v1 = int(v1)
            v2 = int(v2)
            print(calc(v1, oper, v2))
        else:
            print("Invalid input, please input an equation")

user_calc()