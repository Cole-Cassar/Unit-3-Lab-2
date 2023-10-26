import csv

file_obj_csv = open("data.csv")
reader = csv.reader(file_obj_csv)
for line in reader:
    print(line)
