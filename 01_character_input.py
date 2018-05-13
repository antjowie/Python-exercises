import datetime


def main():
    # Get user specific data
    name = input('Hello, what is your name? ')
    age = input('What is your age? ')
    count = int(input('How many times should I repeat the message? '))

    # Calculate the year in which the user will turn 100 years old
    year = 100 - int(age) + datetime.date.today().year

    print(count * (name + ' will turn 100 in the year ' + str(year) + '\n'))


if __name__ == '__main__':
    main()
