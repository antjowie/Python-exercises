birthdays = {
    'James Franklin' : '07/11/1995',
    'Howard Jobson' : '14/03/1982',
    'Anderson Stevens' : '07/13/1975'
}

print('Welcome to the birthday dictionary. We know the birthdays of:','\n'.join(birthdays.keys()),'Who\'s birthday do you want to look up?', sep='\n')

# Convert all first cases to upper cases
name = input().capitalize()
name = [string.capitalize() for string in name.split()]
name = ' '.join(name)

if name not in birthdays:
    print('We do not have any record of the name',name)
else:
    print(f"{name}'s birthday is {birthdays[name]}")