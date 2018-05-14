import sys


with open(sys.argv[1],'rt') as f:
    categories = {}
    for name in f.readlines():
        category = name.split('/')
        category = '/'.join(category[2:-1])
        
        if category in categories:
            categories[category] += 1
        else:
            categories[category] = 1

print('\n'.join(categories))