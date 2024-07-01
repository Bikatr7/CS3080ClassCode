## Kaden Bilyeu
## 2024-06-26
## In-Class 2: Proof of List
## CS 3080-001
## main.py

## built-in libraries
import typing

##-------------------start-of-is_integer()--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def is_integer(value:str) -> typing.Tuple[typing.Union[int, str], bool]:

    """

    This function checks if the input value is an integer or not.

    Parameters:
    value (str): The input value to be checked.

    Returns:
    (int, bool): A tuple containing the value and a boolean value indicating if the input value is an integer or not.S

    """

    try:
        value = int(value)
        return value, True
    
    except ValueError:
        return value, False


##-------------------start-of-main()--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def main():

    user_list = input("Please enter a list of values separated by a space: ").split()
    
    print("-------------------------")
    print("User list:")
    print(user_list, end="\n\n")

    for value in user_list:

        print(value)

        user_list_value, is_int = is_integer(value)
        
        if(is_int):

            user_list[user_list.index(value)] = user_list_value

            print(f"{user_list_value} is an integer.")

main()