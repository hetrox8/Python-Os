import csv

#specify file path
csv_file_path = 'example.csv'

#open the file specified
with open(csv_file_path,'r') as file:
  #create a reader object to read through the CSV file
  csv_reader = csv.DictWriter(file)
#loop through each row in each csv
  for row in csv_reader:
       print(row)