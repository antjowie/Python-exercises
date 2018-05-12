import string
import random

# Give the password a random size
password = ''
for num in range(random.randint(20,30)):
    method = random.randint(0,4)
    if method == 0:
        password += str(random.randint(0,9))
    elif method == 1:
        password += string.ascii_lowercase[random.randint(0,len(string.ascii_lowercase) - 1)] 
    elif method == 2:
        password += string.ascii_uppercase[random.randint(0,len(string.ascii_uppercase) - 1)]
    elif method == 3 or method == 4:
        password += string.printable[random.randint(len(string.ascii_letters+string.digits),len(string.printable)-5)]
    
print (password)