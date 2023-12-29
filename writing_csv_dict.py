import csv

csv_file_path = 'example.csv'

data = [
  ['name', 'age', 'occupation'],
  ['john', '34', 'accountant'],
  ['susan', '28', 'engineer']
]

fieldnames = ['name', 'age', 'occupation']

with open(csv_file_path, 'w', newline='') as file:
  csv_writer = csv.DictWriter(file, fieldnames=fieldnames)

  csv_writer.writeheader

  csv_writer.writerow(data)

print(f'csv file "{csv_file_path}" has been created')