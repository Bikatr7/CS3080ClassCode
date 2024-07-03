## Kaden Bilyeu
## 2024-07-01
## Homework 3: File IO
## CS 3080-001
## main.py

## Instructions:

## Do the following:
## Open the .csv file
## Print the contents of the file
## Create a directory called "To Process"
## Move to that directory
## Create another directory called "Work Copy"
## Take the .csv data and write it to a file called "copy_Content.txt" and save it to the Work Copy directory
## Close the file

## built-in libraries
import os

def main():

## assuming the file is in the same directory as the script
## working directory must be the directory where the script is located
## the working directory must be in-class/3_proof_of_file_io for this to work in my case
## and that the file is named 'csv_file.csv'
## will upload the file to the assignment as well

    ## skipping using csv module for this assignment as we are only copying the contents of the file

    contents = []

    try:

        with open('csv_file.csv', 'r') as file:
            for line in file:
                print(line)
                contents.append(line)

    except FileNotFoundError:
        print('File not found')
        exit(1)

    if(not os.path.exists('To Process')):
        os.mkdir('To Process')

    os.chdir('To Process')

    if(not os.path.exists('Work Copy')):
        os.mkdir('Work Copy')

    os.chdir('Work Copy')

    with open('copy_Content.txt', 'w') as file:
        file.writelines(contents)

if(__name__ == '__main__'):
    main()