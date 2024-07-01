## Kaden Bilyeu
## 2024-06-12
## In-Class 1: Proof of Sum
## CS 3080-001
## main.py

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

##-------------------start-of-main()--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def main() -> None:

    result_1 = sum(1, 2)
    result_2 = sum(1.0, 2.0)

    print(result_1)
    print(result_2)

main()