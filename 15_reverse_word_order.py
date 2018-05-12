def reverse(string):
    # reversed_words = string[::-1].split()
    # return (' '.join([a[::-1] for a in reversed_words]))
    return ' '.join(string.split()[::-1])

string = 'My name is Michele'
print(reverse(string))