import random

# a = [random.randint(1,20) for val in range(20)]
# b = [random.randint(1,20) for val in range(15)]
a = random.sample(range(1,30),20)
b = random.sample(range(1,30),15)


# a = [1, 1, 2, 3,    5,       8,                13, 21, 34, 55, 89]
# b = [1, 2,    3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# ab = [num for num in a for num2 in b if num == num2]
ab = {num for num in set(a) if num in b}

print(ab)