birthdays = {'Jennie': '1996-01-16', 'Lisa': '1997-03-27', 'Rose': '1997-02-11', 'Jisoo': '1995-01-03'}

while True:
    name = input('Enter Blackpint member name: ').title()
    if name == '':
        break
    
    if name in birthdays:
        print(birthdays[name]+ ' is the birthday of ' + name)
    else:
        print('I do not know the birthday of' + name)

print('Blackpink in your area!')

