## Kaden Bilyeu
## 2024-07-14
## Midterm; Question 5
## CS 3080-001
## 5.py

## Testing and debugging here, final answers will be handwritten on the exam.

## Write a function that takes in an integer. The function will return a Boolean value if the
## number is a prime number. Have the return value displayed before the program finishes
## executing.

def q5_is_prime(num) -> bool:

    if(num <= 1):
        return False
    
    if(num == 2):
        return True
    
    if(num % 2 == 0):
        return False
    
    ## factor checking through odd numbers till the square root of the number
    for i in range(3, int(num**0.5) + 1, 2):
        if(num % i == 0):
            return False
        
    return True

number = int(input("Enter a number to check if it is prime: "))

result = q5_is_prime(number)

print(f"Assertion that {number} is prime: {result}")