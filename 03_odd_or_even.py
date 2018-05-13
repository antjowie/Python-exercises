def main():
    num = int(input('Please enter an number: '))
    check = int(input('Please enter a divider: '))

    if num % check == 0:
        print(num, 'is an factor of', check)
    elif num % 4 == 0:
        print(num, 'is an factor of 4')
    elif num % 2 == 1:
        print(num,'is an odd number')
    else:
        print(num,'is an even number')

    return

if __name__ == '__main__':
    main()