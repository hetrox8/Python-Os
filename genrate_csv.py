import csv

csv_file_path = 'output.csv'

#data to be written to the csv file
data = [
  ['Name', 'Age', 'City'],
  ['John Doe', 30, 'New York'],
  ['suleiman', '20', 'Mombasa']
]

#open the csv file in write mode
with open(csv_file_path,'w', newline='') as file:
  #create csv writer
  csv_writer = csv.writer(file)

  #write the data to the csv file
  csv_writer.writerows(data)

print(f'csv file "{csv_file_path}" has been created')
