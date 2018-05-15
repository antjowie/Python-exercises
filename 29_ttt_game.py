def check_ttt(board_list):
    '''
    Gets a ttt play list and returns the winning number
   -1 - draw
    0 - not finished
    1 - p1 won
    2 - p2 won
    '''
    # Structure of a board_list
    #    [[1, 2, 0],
    #     [2, 1, 0],
    #     [2, 1, 1]]

    # Check rows
    for num in range(3):
        if board_list[num][0] != 0 and board_list[num][0] == board_list[num][1] and board_list[num][1] == board_list[num][2]:
            return board_list[num][0]

    # Check columns
    for num in range(3):
        if board_list[0][num] != 0 and board_list[0][num] == board_list[1][num] and board_list[1][num] == board_list[2][num]:
            return board_list[0][num]

    # Check both diagonals
    if board_list[0][0] != 0 and board_list[0][0] == board_list[1][1] and board_list[1][1] == board_list[2][2]:
        return board_list[0][0]

    if board_list[2][0] != 0 and board_list[2][0] == board_list[1][1] and board_list[1][1] == board_list[0][2]:
        return board_list[2][0]

    if 0 not in board_list[0] + board_list[1] + board_list[2]:
        return -1

    return 0


def number_to_symbol(number):
    if number == 0:
        return ' '
    elif number == 1:
        return 'X'
    elif number == 2:
        return 'O'


def print_ttt(board_list):
    for row in range(3):
        print(' ---' * 3)
        for column in range(3):
            print(f'| {number_to_symbol(board_list[row][column])} ', end='')
        print('|')
    print(' ---' * 3)


def valid_input(player, board_list):
    while True:
        move = input(f'Player {player} (row 1-3,column 1-3): ')
        move.strip(',')
        if len(move) != 2 or move.isnumeric() == False:
            print('Invalid input')
            continue

        move = [int(a) for a in move]
        if (move[0]) < 1 or move[0] > 3 or move[1] < 1 or move[1] > 3:
            print('Input too large or too small')
            continue

        if board_list[move[0] - 1][move[1] - 1] != 0:
            print('Place already taken')
            continue

        board_list[move[0] - 1][move[1] - 1] = player
        return


def main():
    print('Welcome to tic tac toe')
    score = [0, 0]
    while True:
        board = ([[0, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0]])

        turn = 0
        while True:
            turn = turn % 2
            turn = turn + 1
            print_ttt(board)

            valid_input(turn, board)

            state = check_ttt(board)

            if state != 0:
                print_ttt(board)
            if state == 1:
                print('Player 1 won')
                score[0] += 1
            elif state == 2:
                print('Player 2 won')
                score[1] += 1
            elif state == -1:
                print('Draw')
            if state != 0:
                print(f'Score player 1: {score[0]}   player 2: {score[1]}')
                if input('Want to play again? (type exit to stop or enter to continue) ').lower() == 'exit':
                    return
                else:
                    break


if __name__ == '__main__':
    main()
