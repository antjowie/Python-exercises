def main():
    num = int(input("Enter a number that you want the divisor of: " ))

    divisors = range(2,num+1)
    for div in divisors:
        if num % div == 0:
            print(div,'is the divisor of',num)

if __name__ == '__main__':
    main()