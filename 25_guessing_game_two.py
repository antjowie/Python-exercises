from sys import exit


size = int(input('Think of a positive integer below and including: '))
print('1 - lower', '2 - higher', '3 - correct', sep = '\n')
numbers = range(size + 1)

while len(numbers) > 0:
    number = numbers[len(numbers) // 2]
    user = int(input('Is the number you have in mind ' + str(number) + '? '))
    if user == 1:
        numbers = numbers[:len(numbers) // 2]
    elif user == 2:
        numbers = numbers[len(numbers) // 2 + len(numbers) % 2:]
    elif user == 3:
        print('I won! Thanks for playing')
        exit()
    else:
        print('Invalid input!')
        print('1 - lower', '2 - higher', '3 - correct', sep = '\n')

print('You liar')
