## Kaden Bilyeu
## 2024-07-01
## In-Class 3: Proof of File IO
## CS 3080-001
## main.py

def main():

## assuming the file is in the same directory as the script
## the working directory must be in-class/3_proof_of_file_io for this to work in my case
## and that the file is named 'csv_file.csv'
## will upload the file to the assignment as well

    contents = []

    with open('csv_file.csv', 'r') as file:
        for line in file:
            print(line)
            contents.append(line)

    with open('copy_Content.txt', 'w') as file:
        file.writelines(contents)

if(__name__ == '__main__'):
    main()