import random
# import pdb
# user_choice = input()
choices = ['rock', 'scissors', 'paper']
# all_choices = ['rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air', \
#                'paper', 'sponge', 'wolf', 'tree', 'human', 'snake', \
#                'scissors', 'fire']
# choices5 = ['rock','paper','scissors','lizard','spock']


# class


# 7 left 7 right

player = input('Enter your name: ')
print(f'Hello, {player}')
score = 0
rating = open('rating.txt', 'r')
for line in rating:
    if player == line.split(' ')[0]:
        score = int(line.split(' ')[1][:-1])
rating.close()

user_choices = [name for name in input().split(',')]
# user_choices = all_choices
# user_choices = ['rock','paper','scissors','dragon','spock']


# print(user_choices)

print("Okay, let's start")

if user_choices == ['']:
    while True:
        # pdb.set_trace()
        user_choice = input()
        if user_choice == '!exit':
            print('Bye!')
            break
        elif user_choice == '!rating':
            print(f'Your rating: {score}')
        elif user_choice not in choices:
            print('Invalid input')
        else:
            computer_choice = random.choice(choices)
            if user_choice == computer_choice:
                print(f'There is a draw ({computer_choice})')
                score += 50
            elif (user_choice == 'rock' and computer_choice == 'scissors') or \
                (user_choice == 'scissors' and computer_choice == 'paper') or \
                (user_choice == 'paper' and computer_choice == 'rock'):
                print(f'Well done. Computer chose {computer_choice} and failed')
                score += 100
            else:
                print(f'Sorry, but computer chose {computer_choice}')

else:
    # print(user_choices)
    while True:
        # pdb.set_trace()
        user_choice = input()
        if user_choice == '!exit':
            print('Bye!')
            break
        elif user_choice == '!rating':
            print(f'Your rating: {score}')
        elif user_choice not in user_choices:
            print('Invalid input')
        else:
            computer_choice = random.choice(user_choices)
            user_index = user_choices.index(user_choice)
            comp_index = user_choices.index(computer_choice)
            length = len(user_choices) // 2
            # print(length)
            # print(user_index)
            beaten = user_choices[user_index+1:user_index + length + 1]
            # beats = user_choices[user_index + length + 1:]
            if len(beaten) < length:
                beaten += user_choices[:length - len(beaten)]
            # if len(beats) < length:
            #     beats += user_choices[user_index - length:user_index]
            # print(beaten)
            # print(beats)
            if user_choice == computer_choice:
                print(f'There is a draw ({computer_choice})')
                score += 50
            elif computer_choice not in beaten:
                print(f'Well done. Computer chose {computer_choice} and failed')
                score += 100
            else:
                print(f'Sorry, but computer chose {computer_choice}')
#             elif
# all_choices = ['rock', 'gun', 'lighting', 'devil', 'dragon', 'water', 'air', \
#                'paper', 'sponge', 'wolf', 'tree', 'human', 'snake', \
#                'scissors', 'fire']
            # # print(all_choices.index(user_choice))
            # user_index = all_choices.index(user_choice)
            # comp_index = all_choices.index(computer_choice)
            # length = len(user_choices) // 2
            # beaten = all_choices[user_index+1:user_index + length + 1]
            # beats = all_choices[user_index + length + 1:]
            # if len(beaten) < length:
            #     beaten += all_choices[:length - len(beaten)]
            # # if len(beats) < length:
            # #     beats += all_choices[user_index - length:user_index]
            # print(beaten)
            # print(beats)



            # elif (user_choice == 'rock' and computer_choice == 'scissors') or \
            #     (user_choice == 'scissors' and computer_choice == 'paper') or \
            #     (user_choice == 'paper' and computer_choice == 'rock'):
            #     print(f'Well done. Computer chose {computer_choice} and failed')
            #     score += 100
            # else:
            #     print(f'Sorry, but computer chose {computer_choice}')







# import random

# user_choice = input()

# x_beats_y = {
#     'rock':'scissors',
#     'paper': 'rock',
#     'scissors': 'paper'
# }
# computer_choice = random.choice(list(x_beats_y.keys()))

# if user_choice == computer_choice:
#     print(f'It\'s a tie. Computer chose {computer_choice}')
# elif x_beats_y[user_choice] == computer_choice:
#     # user_choice beats computer_choice
#     print(f'Well done. Computer chose {computer_choice} and failed')
# else:
#     print(f'Sorry, but computer chose {computer_choice}')