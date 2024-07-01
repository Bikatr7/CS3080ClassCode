## Kaden Bilyeu
## 2024-06-12
## Homework 1: Introduction to Functions
## CS 3080-001
## main.py

## Greetings Grader, my name is Kaden. I've been coding in python for a while, and I typically document my code with docstrings, and use extensive type hints. 
## I hope you enjoy grading my code, and you have a great day!

## An example of some python code I've written before to help prove that this isn't simply auto-generated code:
## https://github.com/Bikatr7/Kudasai

## built-in libraries
import typing

## custom modules
from homework1 import sum, sub, mul, div

##-------------------start-of-convert_input()--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def convert_input(user_input:str) -> typing.Union[int, float]:
    
    """

    This function takes a string as input and returns an integer or float.

    Parameters:
    user_input (str) : The string to be converted.

    Returns:
    (int | float) : The integer or float value of the string.

    """

    return float(user_input) if '.' in user_input else int(user_input)

##-------------------start-of-main()--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def main() -> None:

    ## convert user input to numbers based on the presence of a decimal point1
    first_user_number = convert_input(input("Please enter the first number: "))
    second_user_number = convert_input(input("Please enter the second number: "))

    print()

    ## all functions are forced to return an integer.

    ## display the results of the four basic arithmetic operations
    print(f"The sum of the two numbers is: {sum(first_user_number, second_user_number)}")
    print(f"The difference of the two numbers is: {sub(first_user_number, second_user_number)}")
    print(f"The product of the two numbers is: {mul(first_user_number, second_user_number)}")
    print(f"The quotient of the two numbers is: {div(first_user_number, second_user_number)}")

##-------------------end-of-main()--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

main()