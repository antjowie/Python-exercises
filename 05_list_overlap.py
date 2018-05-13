import datetime
import random


def main():
    seed = datetime.date.today().timetuple()
    seed = seed[0] + seed[1] + seed[2]

    a = []
    b = []

    i = 0
    while i < 10:
        a.append(random.randrange(10))
        if i < 8:  
            b.append(random.randrange(10))
        i += 1

    print('a:',a)
    print('b:',b)

    a.extend(b)
    a.sort()
    merged = {}
    for item in a:
        if item in merged:
            merged[item] += 1
        else:
            merged[item] = 1

    dup = []
    for num in merged:
        if merged[num] > 1:
            dup.append(num)

    print('ab:',a)
    print('dup:',dup)

if __name__ == '__main__':
    main()