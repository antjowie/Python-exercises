
def get_input(message):
    '''
    Asks for an input and validates it
    until a correct input is given
    '''

    while True:
        # Validate input
        string = input(message)
        if string[0].isnumeric() == False:
            print('The input should be an integer.',
                  string[0], 'is not an integer')
            continue
        string = int(string[0])

        if string == 1:
            return 'rock'
        elif string == 2:
            return 'paper'
        elif string == 3:
            return 'scissors'

        print('An invalid integer has been given, be sure that the integer is one of the following',
              '1: Rock', '2: Paper', '3: Scissors', sep='\n')


def main():
    print('Welcome to Rock Paper Scissors!', 'You will write your move as a number',
          '1: Rock', '2: Paper', '3: Scissors', sep='\n')

    while True:
        # Get input
        p1 = get_input('Player 1\'s move: ')
        p2 = get_input('Player 2\'s move: ')

        # Get result
        if p1 == p2:
            print('It\'s a draw')

        else:
            p1_wins = False
            if p1 == 'rock' and p2 == 'scissors':
                p1_wins = True

            elif p1 == 'paper' and p2 == 'rock':
                p1_wins = True

            elif p1 == 'scissors' and p2 == 'paper':
                p1_wins = True

            if p1_wins:
                print('Player 1 has won with', p1)
            else:
                print('Player 2 has won with', p2)

        # Ask for another round
        if str(input('Want to play again?(y/n)')).lower() == 'n':
            break

    print('Thank you for playing!')


if __name__ == '__main__':
    main()
