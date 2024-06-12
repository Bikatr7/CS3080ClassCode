## built-in libraries
import typing

##-------------------start-of-sum()--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def sum(first_number:typing.Union[int, float], second_number:typing.Union[int, float]) -> int:

    """
    
    This function takes two numbers as input and returns the sum of the two numbers.

    Parameters:
    first_number (int | float): The first number to be added.
    second_number (int | float): The second number to be added.

    Returns:
    int: The sum of the two numbers.

    """
    
    first_number = int(first_number)
    second_number = int(second_number)

    return first_number + second_number

##-------------------start-of-sub()--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def sub(first_number:typing.Union[int, float], second_number:typing.Union[int, float]) -> int:

    """
    
    This function takes two numbers as input and returns the difference of the two numbers.

    Parameters:
    first_number (int | float): The first number to be subtracted.
    second_number (int | float): The second number to be subtracted.

    Returns:
    int: The difference of the two numbers.

    """
    
    first_number = int(first_number)
    second_number = int(second_number)

    return first_number - second_number

##-------------------start-of-mul()--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def mul(first_number:typing.Union[int, float], second_number:typing.Union[int, float]) -> int:

    """
    
    This function takes two numbers as input and returns the product of the two numbers.

    Parameters:
    first_number (int | float): The first number to be multiplied.
    second_number (int | float): The second number to be multiplied.

    Returns:
    int: The product of the two numbers.

    """
    
    first_number = int(first_number)
    second_number = int(second_number)

    return first_number * second_number

##-------------------start-of-div()--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def div(first_number:typing.Union[int, float], second_number:typing.Union[int, float]) -> int:

    """
    
    This function takes two numbers as input and returns the division of the two numbers.

    Parameters:
    first_number (int | float): The first number to be divided.
    second_number (int | float): The second number to be divided.

    Returns:
    int: The division of the two numbers.

    """
    
    first_number = int(first_number)
    second_number = int(second_number)

    return int(first_number / second_number)