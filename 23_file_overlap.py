import sys


list1 = []
list2 = []

with open(sys.argv[1],'r') as f1:
    list1 = [int(num) for num in f1.readlines()]
with open(sys.argv[2],'r') as f2:
    list2 = [int(num) for num in f2.readlines()]

overlap = [num for num in list1 if num in list2]

print(overlap)