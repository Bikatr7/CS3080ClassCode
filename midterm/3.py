## Kaden Bilyeu
## 2024-07-14
## Midterm; Question 3
## CS 3080-001
## 3.py

## Testing and debugging here, final answers will be handwritten on the exam.

## Write a program that opens a file. Then, input a list of integers from the command line to
## be cryptographically changed. For every integer, XOR it with the number 7 and then print
## the result and write it to the file.

def q3_xor_thingy():
    filename = input("Enter the filename to write to: ")
    integers = input("Enter a list of integers separated by spaces: ").split()
    
    ## list comprehension my beloved

    integers = [int(i) for i in integers]

    write_list = [f"{i} XOR 7 = {i ^ 7}\n" for i in integers]
    
    with open(filename, 'w', encoding='utf-8') as file:
        file.writelines(write_list)

q3_xor_thingy()
