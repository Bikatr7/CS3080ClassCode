## Kaden Bilyeu
## 2024-07-14
## Midterm; Question 2
## CS 3080-001
## 2.py

## Testing and debugging here, final answers will be handwritten on the exam. 

## Write a small program that takes multiple inputs, not on one command line, from the
## user until the string END is input. When END is input, print the list of all the values that
## were input into the console.

def q2_collect_inputs():
    
    inputs = []
    
    ## assuming case sensitivity is not an issue

    while True:
        user_input = input("Enter a value (or type 'END' to finish): ")
        if(user_input == 'END'):
            break

        inputs.append(user_input)

    print("Collected inputs : ", inputs)

q2_collect_inputs()
