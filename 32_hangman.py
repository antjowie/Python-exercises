import random


def check_input(message, guesses):
    while True:
        guess = input(message).upper()

        for char in guess:
            if char in guesses:
                print('You already guessed this letter:', guesses)
                continue

        return guess


def update_user_string(correct_word, guesses):
    string = ''
    for char in correct_word:
        if char in guesses:
            string += char
        else:
            string += '_'

    return string


def print_hangman(parts):
    if parts == 0:
        string = '''
                    _O_
                     |
                    / \\
                 '''
    elif parts == 1:
        string = '''
                    _ _
                     |
                    / \\
                 '''
    elif parts == 2:
        string = '''  
                      _
                     |
                    / \\
                 '''
    elif parts == 3:
        string = '''
                      
                     |
                    / \\
                '''
    elif parts == 4:
        string = '''
                       
                        
                    / \\
                '''
    elif parts == 5:
        string = '''
                    
                      
                      \\
                '''
    print(string)


with open('sowpods.txt', 'r') as f:
    words = [word.strip() for word in f.readlines()]


print('Welcome to Hangman!')

play = True
while play == True:
    word = words[random.randint(0, len(words)-1)]
    string = len(word)*'_'
    guesses = []
    attempts = 6

    print('A new word has been selected! It is ', len(
        word), ' letters long!\n', string, sep='')

    while string != word:
        guess = check_input('Make a guess (or exit to give up): ', guesses)
        if guess == 'EXIT':
            print('You gave up, the word was', word.lower())
            string = word

        for letter in guess:
            if letter in word:
                print('Correct!')
            else:
                attempts -= 1
                attempt_string = 'attempts'
                if attempts == 1:
                    attempt_string = 'attempt'
                elif attempts == 0:
                    print('You lost!')
                    string = word
                    print('The word was', word.lower())
                    break
                print('Incorrect!')
                print_hangman(attempts)

            guesses.append(letter)
            guesses = sorted(guesses)
            string = update_user_string(word, guesses)
            print(string)

            if string == word:
                print('You won!')
                break

    if play == True and input('Want to play again? (no to stop) ').lower() == 'no':
        play = False
