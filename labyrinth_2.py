import random

map_width = 0
map_height = 0


difficulty_level = input(f'"Choose a game level("l" for low, "m" for medium, "h" for hard"): ').lower()
match difficulty_level:
    case "l": 
        print("You will play on small area")
        map_width = 5
        map_height = 5
    case "m":
        print("You will play on medium area")
        map_width = random.randint(6,10)
        map_height = random.randint(6,10)
    case "h":
        print("You will play on large area")
        map_width = random.randint(11,15)
        map_height = random.randint(11,15)
    case _:
        inform = print("Wrong character! Run game one more time if you wish to play again")
        exit()

x_key = random.randint(1, map_width)
y_key = random.randint(1, map_height)

key = [x_key,y_key]

position_x = 0
position_y = 0

player_position = [position_x, position_y]

print(f'Key location: {key}')

def tips():
    result_x = abs(key[0]-player_position[0])
    result_y = abs(key[1]-player_position[1])

    sum_up = (result_x,result_y)

    if sum(sum_up) < 2: print("Very hot!")
    elif 2 < sum(sum_up) < 4: print("Hot!")
    elif 3 < sum(sum_up) < 5: print("Cold!")
    else: print("Very Cold!")
            
    print(f'Your position in labirynt : {player_position}')


while player_position != key:
    print()
    move = input("Choose 'W', 'S', 'A', 'D' to move in this direction, Q for quit the game: ")
    if move.lower() == 'w':
        player_position[1] += 1
        if player_position[1] > map_height:
            print('You hit a wall!')
            player_position[1] = map_height
        tips()
    
    elif move.lower() == 's':
        player_position[1] -= 1
        
        if player_position[1] < 0:
            print()
            print('You hit a wall!')
            player_position[1] = 0
        tips()

    elif move.lower() == 'a':
        player_position[0] -= 1

        if player_position[0] < 0:
            print()
            print('You hit a wall!')
            player_position[0] = 0
        tips()
        
    elif move.lower() == 'd':
        player_position[0] += 1
        if player_position[0] > map_width:
            print()
            print('You hit a wall!')
            player_position[0] = map_width
        tips()

    elif move.lower() == 'q':
        quit()

    else:
        move.lower() == ''
        print("Quo Vadis? Use the correct buttons")
print(f"Congrats! You find a key!!!, Key was hidden on position {key}")

