file_obj_csv = open("data.csv")
# csv_data = file_obj_csv.read()
file_obj_csv.readline()
for line in file_obj_csv:
    columns = line.split(",")
    if len(columns) >= 10:
        temp = float(columns[9].replace('"', ''))
        print(temp)
