def check_input(message,guesses):
    while True:
        guess = input(message).upper()[0]

        if guess in guesses:
            print('You already guessed this letter:',guesses)
            continue

        return guess


def update_user_string(correct_word,guesses):
    string = ''
    for char in correct_word:
        if char in guesses:
            string += char
        else:
            string += '_' 

    return string



word = 'EVAPORATE'
string = len(word)*'_'
guesses = []

print('Welcome to Hangman!')
print(string)

while True:
    guess = check_input('Make a guess: ',guesses)
    if guess in word:
        print('Correct!')
    else:
        print('Incorrect!')
    guesses.append(guess)
    string = update_user_string(word,guesses)
    print(string)
    if string == word:
        print('You won!')
        break
    