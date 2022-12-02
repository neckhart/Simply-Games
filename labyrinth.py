import random

map_width = int(input('Write width of your map: '))
map_height = int(input('Write height of your map: '))

x_key = random.randint(0, map_width)
y_key = random.randint(0, map_height)

key = [x_key,y_key]
print(f'Key position : {key}')

position_x = 0
position_y = 0

player_position = [position_x, position_y]


while player_position != key:

    move = input("Choose 'W', 'S', 'A', 'D' to move in this direction: ")
    if move.lower() == 'w':
        player_position[1] += 1
        if player_position[1] > map_height:
            print('You hit a wall')
            player_position[1] = map_height
        print(f'Your position in labirynt : {player_position}')

    elif move.lower() == 's':
        player_position[1] -= 1
        
        if player_position[1] < 0:
            print('You hit a wall')
            player_position[1] = 0
        print(f'Your position in labirynt : {player_position}')

    elif move.lower() == 'a':
        player_position[0] -= 1

        if player_position[0] < 0:
            print('You hit a wall')
            player_position[0] = 0
        print(f'Your position in labirynt : {player_position}')
        
    elif move.lower() == 'd':
        player_position[0] += 1
        if player_position[0] > map_width:
            print('You hit a wall')
            player_position[0] = map_width
        print(f'Your position in labirynt : {player_position}')

    elif move.lower() == 'q':
        quit()

    else:
        move.lower() == ''
        print("Quo Vadis?")
print(f"Congrats! You find a key!!!, Key was hidden on position {key}")