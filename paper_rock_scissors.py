from random import choice
print()
name = input('Please write your name: ')
welcome = print(f'Welcome on a board : {name}!')
print()
number_of_games = int(input('How many games would like to play? '))
print()

def game(x): # for paramter x player send argument == number_of_games
   # 1. Initialize the variables
    number_of_loops = 0
    
    computer_scores = 0
    user_scores = 0
    
    # 2.Loop ends if achive number equles number_of_games
    while number_of_loops != number_of_games:
        number_of_loops += 1
        user_choice = input(f"Choose 'r' for rock, 'p' for paper and 's' for scissors or enter for quit the game ").lower()
        computer_choice = choice(['r', 'p', 's'])
        print(f'{name} : {user_choice} Computer choose : {computer_choice}')
    # 3.Whole logic in 'if' statments
        if user_choice == 'r' and computer_choice == 'p':
            computer_scores += 1
            print('You lose')
        elif user_choice == 'r' and computer_choice == 's':
            user_scores += 1
            print('You win')
        elif user_choice == 'p' and computer_choice == 'r':
            user_scores += 1
            print('You win')
        elif user_choice == 'p' and computer_choice == 's':
            computer_scores += 1
            print('You lose')
        elif user_choice == 's' and computer_choice == 'r':
            computer_scores += 1
            print('You lose')
        elif user_choice == 's' and computer_choice == 'p':
            user_scores += 1
            print('You win')
        elif user_choice == computer_choice:
            print('Tie!')
        else:
            quit()

    # Print score result for the end
    print(f'Computer: {computer_scores} vs {name}: {user_scores}')
    
game(number_of_games)