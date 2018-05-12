def fibonacci(count):
    '''
    Generates a list of 'count' Fibonacci numbers
    '''
    numbers = [1,1]
    if count < 2:
        del numbers[count : 2]
    while count > 2:
        numbers.append(numbers[-2]+numbers[-1])
        count -= 1
    return numbers


count = int(input('How many fibonacci numbers do you want to generate? '))
print (fibonacci(count))
