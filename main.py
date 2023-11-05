import sys
file_obj_csv = open("data.csv")
# csv_data = file_obj_csv.read()
file_obj_csv.readline()
for line in file_obj_csv:
    columns = line.split(",")
    if len(columns) >= 10:
        temp = float(columns[9].replace('"', ''))
        print(temp)
print("Loading golf.exe . . . \n ... \n ... \n ...")

print("Welcome to the golf minigame!")
player = input("How many players? (1-2)>>> ")
if int(player) > 2:
    print("Please select a number lower than or equal to 2")
    sys.exit()
holes = input("How many holes? (Max 18)>>> ")
if int(holes) > 18:
    print("Please select a number lower than or equal to 18")
    sys.exit()
golf_obj = open("golf game.txt", "w")
golf_obj.write(f"Welcome to the golf minigame!\n Players: {player} \n Number of holes: {holes} \n Now loading your game . . . \n Error: Memory access violation. Please contact administration")




