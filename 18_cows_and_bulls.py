import random


def format_input(message, min_length=4):
    '''
    Trims whitespaces and returns string lowercase.
    '''
    while True:
        i_string = input(message)
        i_string = i_string.lower()
        i_string = i_string.replace(' ', '')

        if len(i_string) >= min_length and (len(set(i_string)) == 0 or len(set(i_string)) == 4):
            return i_string
        print('Your input is incorrect, it should at least have a length of', min_length,'and no duplicates')


def check_input(number, user_value):
    '''
    Expects 2 integers or strings of same 
    length. Compares user value and returns
    a tupple of cows and bulls
    '''
    number = str(number)
    user_value = str(user_value)

    bulls = 0
    for char in user_value:
        bulls += number.count(char)

    cows = len([a for a in range(len(min(user_value, number)))
                if user_value[a] == number[a]])
    return (cows, bulls)


def main():
    print('Welcome to the Cows and Bulls Game!\nYou can always type \'quit\' to stop playing')
    has_played = False

    while True:
        count = 0
        number = ''.join(list([str(a) for a in random.sample(range(10), 4)]))
        print('A random number of 4 unique digits has been generated')

        while True:
            count += 1

            # Validate input and check if player wants to stop
            string = format_input(':')[:4]
            if string == 'quit':
                if has_played == False:
                    print('You gave up after', count, 'attempts, how sad (it was',number,'by the way)')
                else:
                    print('Thank you for playing.')
                return

            # Check if player has guessed right
            cows, bulls = check_input(number, string)
            if cows == 4:
                break

            # Change verb
            s_cows = 'cows'
            if cows == 1:
                s_cows = 'cow'
            s_bulls = 'bulls'
            if bulls == 1:
                s_bulls = 'bull'

            print('\t\t{}\t{}: {} | {}: {}'.format(
                string, s_cows, str(cows), s_bulls, str(bulls)))

        print('Congratulations, the number was', number +
              '.', 'It took you', count, 'attempts.')
        if format_input('Press enter to play again or \'quit\' to stop: ', 0) == 'quit':
            return


if __name__ == '__main__':
    main()
