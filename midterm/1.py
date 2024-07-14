## Kaden Bilyeu
## 2024-07-14
## Midterm; Question 1
## CS 3080-001
## 1.py

## Testing and debugging here, final answers will be handwritten on the exam. 

## Write a small program that takes in 5 exact inputs from the user in the order of string, int,
## string, float, float. If there are values added that are not to that specification, stop the
## process and display "Incorrect input detected"

def q1_get_inputs():

    ## assuming strings *can* be numbers and floats but not vice versa

    try:
        str_input1 = input("Please enter a string: ")
        int_input = int(input("Please enter an integer: "))
        str_input2 = input("Please enter another string: ")
        float_input1 = float(input("Please enter a float: "))
        float_input2 = float(input("Please enter another float: "))
        print("Inputs accepted:", str_input1, int_input, str_input2, float_input1, float_input2)

    except ValueError:
        print("Incorrect input detected")

q1_get_inputs()
