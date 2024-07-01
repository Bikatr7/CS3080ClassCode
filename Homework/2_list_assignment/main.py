## Kaden Bilyeu
## 2024-06-26
## Homework 2: List Assignment
## CS 3080-001
## main.py

## built-in libraries
import typing

##-------------------start-of-convert_string_to_determined_type()--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def convert_string_to_determined_type(value:str) -> typing.Union[int, float, str]:

    """
    
    This function will convert a string to an integer or float if possible. If not possible, it will return the string as is.

    Parameters:
    value (str): The string value to be converted.

    Returns:
    typing.Union[int, float, str]: The converted value.

    """

    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:
            return value


##-------------------start-of-main()--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def main():

    user_list = input("Please enter a list of values separated by a space: ").split()

    if(len(user_list) == 0):
        print("List is empty.")
        return
    
    [print(f"{value}\n{type(value).__name__}") for value in user_list]

    ## so i could use like a for range loop and change in place but i'm lazy

    for value in user_list:
        converted_value = convert_string_to_determined_type(value)
        user_list[user_list.index(value)] = converted_value
        print(f"{converted_value}\n{type(converted_value).__name__}")
        

main()