import random 


def set_dup(items):
    return [a for a in set(items)]

def loop_dup(items):
    a = []
    for num in items:
        if num not in a:
            a.append(num)
    return a


a = sorted([random.randint(0,10) for num in range(0,20)])
print(a)
print(set_dup(a))
print(loop_dup(a))