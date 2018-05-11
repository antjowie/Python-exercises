import random


def main():
    print('Welcome to the guess game')
    while True:
        # Generate a random number and setting up game related vars
        rand = random.randint(1, 9)
        count = 1

        print('A number between 1 and 9 has been generated')
        while True:
            # Validate guess
            guess = input("Your guess " + str(count) + ': ')
            if guess.isnumeric() == False:
                print('Your guess should be an integer')
                continue

            # Check input
            guess = int(guess)
            if guess == rand:
                print('Correct!, it took you', count, 'attempts to guess right')
                break
            elif guess > rand:
                print('Your guess is too high')
            elif guess < rand:
                print('Your guess is too low')

            count += 1

        if str(input('Type exit if you want to quit or nothing to keep on playing ')).lower() == 'exit':
            break


if __name__ == '__main__':
    main()
