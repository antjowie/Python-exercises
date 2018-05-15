def check_ttt(board_list):
    '''
    Gets a ttt play list and returns the winning number
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

    return 0

def print_winner(board_list):
    winner = check_ttt(board_list)

    if winner == 0:
        print('No winner')

    elif winner == 1:
        print('Player 1 wins')

    elif winner == 2:
        print('Player 2 wins')

def main():
    winner_is_2 = [[2, 2, 0],
        [2, 1, 0],
        [2, 1, 1]]

    winner_is_1 = [[1, 2, 0],
        [2, 1, 0],
        [2, 1, 1]]

    winner_is_also_1 = [[0, 1, 0],
        [2, 1, 0],
        [2, 1, 1]]

    no_winner = [[1, 2, 0],
        [2, 1, 0],
        [2, 1, 2]]

    also_no_winner = [[1, 2, 0],
        [2, 1, 0],
        [2, 1, 0]]

    print_winner(winner_is_2)
    print_winner(winner_is_1)
    print_winner(winner_is_also_1)
    print_winner(no_winner)
    print_winner(also_no_winner)

if __name__ == '__main__':
    main()