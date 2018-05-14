import sys
import random


def binary_contains(sorted_list,element):
    index = len(sorted_list) // 2
    print(sorted_list)
    if sorted_list[index] == element:
        return True
    elif index == 0:
        return False
    elif sorted_list[index] > element:
        return binary_contains(sorted_list[:index],element)
    elif sorted_list[index] < element:
        return binary_contains(sorted_list[index:],element)


a = sorted(random.sample(range(10),5))

print(binary_contains(a,int(sys.argv[1])))