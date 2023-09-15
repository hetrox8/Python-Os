# to read files in programming we can use python
# step 1. python3
# step 2. ensure your are in the right directory for the file you want to read

file = open("file name") 
# file = open ("scripts.py")

print(file.readline()) # this will print a single line in the file
print(file.read()) # this will print all lines in the file

# always remember to close the file with the close()

file = open ("scripts.py")
print(file.read())

#close file.close()

# automatically close file using with

with open("scripts.py") as file:
    print(file.read())

#we can print desired characters we want

with open("scripts.py") as file:
    print(file.read(10)) #we can pass desired no. of character to be printed


with open("scripts.py") as file:
    read_no = 100

    print(file.read(read_no))
