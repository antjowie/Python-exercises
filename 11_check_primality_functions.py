value = int(input('Enter a number: '))
primes = []

# Get all primes
for num in range(1,value+1):
    # Calculate all values which it can divide by
    divisors = [number for number in range(1,num + 1) if num % number == 0]
    
    # Check if the value is a prime and divisable by our input
    if len(divisors) <= 2 and value % num == 0:
        primes.append(num)
    print ('Calculating number', num,'till number', value, '[progress is', int(num/value*100),'per cent]')

print('List of primes', value, 'is divisable by:',primes)