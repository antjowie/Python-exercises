import json
from collections import Counter


with open('birthdays.json', 'r') as f:
    birthdays = json.load(f)

print('Welcome to the birthday dictionary')

while True:

    print('We know the birthdays of:', '\n'.join(sorted(birthdays.keys())),
          '1 - Add a person',
          '2 - Remove a person',
          '3 - Get birthday of a person',
          '4 - List birthday occurences in months',
          '0 - Save and exit',
          sep='\n')

    # Convert all first cases to upper cases
    number = input('# ')
    if number.isnumeric() == False:
        print('Your option should be a number')
        continue
    number = int(number[0])
    if number == 0:
        break

    elif number == 4:
        # Convert numeric dates to alphabetic
        months = []
        for birthday in birthdays.values():
            birthday = birthday.split('/')[1]
            if birthday == '01':
                months.append('January')
            elif birthday == '02':
                months.append('February')
            elif birthday == '03':
                months.append('March')
            elif birthday == '04':
                months.append('April')
            elif birthday == '05':
                months.append('May')
            elif birthday == '06':
                months.append('June')
            elif birthday == '07':
                months.append('July')
            elif birthday == '08':
                months.append('August')
            elif birthday == '09':
                months.append('September')
            elif birthday == '10':
                months.append('October')
            elif birthday == '11':
                months.append('November')
            elif birthday == '12':
                months.append('December')
        print(Counter(months))

    elif number <= 3 and number >= 1:
        name = input('Insert the name of the person: ').capitalize()
        name = [string.capitalize() for string in name.split()]
        name = ' '.join(name)

        # Add person
        if number == 1:
            # Check it the entry did not already exist
            overwrite = True
            if name in birthdays:
                overwrite = False
                if input('This person already exists inside the record, want to overwrite it? (Type yes to overwrite) ').lower() == 'yes':
                    overwrite = True

            # Format date
            if overwrite == True:
                birthday = input(
                    'Enter birthday data in the following format (dd mm yyyy): ')
                birthday = birthday.split()
                if len(birthday) != 3:
                    print('Invalid format')

                else:
                    birthday[0] = birthday[0].zfill(2)[:2]
                    birthday[1] = birthday[1].zfill(2)[:2]
                    birthday[2] = birthday[2].zfill(4)[:4]
                    birthday = '/'.join(birthday)
                    birthdays[name] = birthday

        # Remove a person
        if number == 2:
            if name in birthdays:
                print(name, 'successfully removed')
                del birthdays[name]
            else:
                print('Information about', name, 'has not been found')

        # Get a persons birthday
        if number == 3:
            if name not in birthdays:
                print('We do not have any record of the name', name)
            else:
                print(f"{name}'s birthday is {birthdays[name]}")

    else:
        print('Unknown option entered')

with open('birthdays.json', 'w') as f:
    json.dump(birthdays, f)
