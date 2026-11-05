counts = {'yes': 0, 'no':0}

for i in range(4):
    answer = input('Enter a yes or no: ').lower()

    if answer == 'yes' or answer == 'no':
        counts[answer] = counts[answer] + 1
    else:
        print('Invalid input')

print('Results: ', counts)

        

