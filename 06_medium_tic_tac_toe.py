import time

cells = ' ' * 9
values = [value for value in cells]
winner = ''

def create_matrix():
    global matrix
    a = 0
    b = 3
    matrix = []
    for i in range(3):
        matrix.append([])
        for j in ''.join(values[a:b]):
            matrix[i].append(j)
        a += 3
        b += 3
    print('---------')
    time.sleep(0.1)
    for i in range(3):
        print('| ' + ' '.join(matrix[i]) + ' |')
        time.sleep(0.1)
    print('---------')

create_matrix()

empty_cell = [13, 23, 33, 12, 22, 32, 11, 21, 31]

def user_input():
    the_index = None
    coordinates = input('Enter the coordinates: ').split()
    coord = int(''.join(coordinates))
    if int(coord) in empty_cell:
        the_index = empty_cell.index(int(coord))
    else:
        print("Coordinates should be from 1 to 3!")
        the_index = user_input()
    return the_index

def check_winner():
    global winner
    while True:
        # we find if X or O wins on a row
        result = ''
        for i in range(3):
            for values in enumerate(matrix[i]):
                result += values[1]
                if result == 'XXX' or result == 'OOO':
                    # print(f'{result[1]} wins')
                    winner = result[1]
                    result = ''
                elif len(result) == 3:
                    result = ''

        # we reverse the matrix for the columns
        reversed_matrix = []
        for i in range(3):
            reversed_matrix.append([])
            for j in range(3):
                reversed_matrix[i].append(matrix[j][i])

        # we find if X or O wins on a reversed matrix
        for i in range(3):
            for values in enumerate(reversed_matrix[i]):
                result += values[1]
                if result == 'XXX' or result == 'OOO':
                    winner = result[1]
                    result = ''
                elif len(result) == 3:
                    result = ''

        # we find if X or O wins on the left diagonal
        left_diagonal = [r[i] for i, r in enumerate(matrix)]
        right_diag = []
        j = 2
        for i in range(3):
            right_diag.append(matrix[i][j])
            j -= 1

        if ''.join(left_diagonal) == 'XXX' or \
        ''.join(right_diag) == 'XXX':
            winner = 'X'
            result = 'XXX'
        elif ''.join(left_diagonal) == 'OOO' or \
            ''.join(right_diag) == 'OOO':
            winner = 'O'
            result = 'OOO'
        break

    if winner == 'X':
        print('X wins')
        return True
    elif winner == 'O':
        print('O wins')
        return True

turn = 1
while True:
    try:
        if ' ' not in values:
            print('Draw')
            break
        the_index = user_input()
        if values[the_index] != ' ':
            print('This cell is occupied! Choose another one!')
        else:
            if turn == 1:
                values[the_index] = 'X'
                create_matrix()
                turn = 0
                if check_winner():
                    break
            else:
                values[the_index] = 'O'
                create_matrix()
                turn = 1
                if check_winner():
                    break
    except ValueError:
        print('You should enter numbers!')
