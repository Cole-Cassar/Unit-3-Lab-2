import sys
file_obj_csv = open("data.csv")
# csv_data = file_obj_csv.read()
file_obj_csv.readline()
for line in file_obj_csv:
    columns = line.split(",")
    if len(columns) >= 10:
        temp = float(columns[9].replace('"', ''))
        print(temp)
# CVS Temperature portion
print("Loading golf.exe . . . \n ... \n ... \n ...")
print("Welcome to the golf minigame!")
player_1 = 1
player_2 = 2
player = input("How many players? (1-2)>>> ")
if int(player) > 2:
    print("Please select a number lower than or equal to 2")
    sys.exit()
holes = input("How many holes? (Max 18)>>> ")
if int(holes) > 18:
    print("Please select a number lower than or equal to 18")
    sys.exit()
golf_obj = open("Golf game.txt", "w")
golf_obj.write(f"Welcome to the golf minigame!\n Players: {player} \n Number of holes: {holes} \n Now loading your game . . .")
golf_score = open("Golf Score.txt", 'w')
golf_score.write(f"""
=========
Score: 38    
=========\n Thank you for playing!""")
sys.exit
# Golf Game portion. Get player input >> Output player input. Create 2 seperate files for Golf data and Golf score.




