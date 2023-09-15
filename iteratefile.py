with open("scripts.py") as file:
    for line in file:
        print(line.upper())
#the above command will print the file lines but with extra spaces
#to solve this we can use the below

with open("scripts.py") as file:
    for line in file :
        print (line.strip().upper())

#reading file content even with file closed
#we use the readlines() and save in a list /variable
file = open("scripts.py")
lines = file.readlines()

file.close()  #file is closed but we can read the contents
lines.sort() #this sorts the contents alphabetically