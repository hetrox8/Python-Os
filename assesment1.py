#creating a directory in a directory and a file and listing files
import os

def new_directory(directory, filename):
  #check if folder exitst
  if os.path.isdir(directory) == false:
    os.path.exists('scripts.py')
    os.makedirs(directory)


  #create new file in the  new folder
  os.chdir(directory)
  with open( 'scripts.py','w') as file:
    pass

  #return list of files 
  os.listdir()
  print(new_directory("python programs", "scripts.py"))

  #QThe file_date function creates a new file in the current working directory, checks the date that the file was modified, and returns just the date portion of the timestamp 
 #in the format of yyyy-mm-dd. Fill in the gaps to create a file called "newfile.txt" and check the date that it was modified

import os
import datetime

def file_date(filename):
    # Create the file in the current directory
    with open(filename, 'w') as file:
        pass  # This line creates an empty file

    # Get the last modification time of the file
    timestamp = os.path.getmtime(filename)

    # Convert the timestamp into a readable format, then into a string
    modifytime = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')

    # Return just the date portion 
    # Hint: how many characters are in “yyyy-mm-dd”? 
    return modifytime

# Example usage
print(file_date("newfile.txt"))
