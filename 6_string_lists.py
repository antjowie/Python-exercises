def main():
    string = input("Please enter a string: ")
    
    # Can also use string[::-1]
    if string == ''.join(list(reversed(string))):    
        print('The string is a palindrome')
    else:
        print('The string is a palindrome')

if __name__ == '__main__':
    main()