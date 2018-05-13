import sys
import os

os.chdir(sys.argv[1])

items = [item for item in os.listdir() if item.split('_')[0].isnumeric()]
input('\n'.join(items) + '\nDo you wanna affect the following items? (press enter to continue)')

for item in items:
    number,name = item.split('_',1)
    number = number.zfill(2)
    string = '{}_{}'.format(number,name)
    os.rename(item,string)