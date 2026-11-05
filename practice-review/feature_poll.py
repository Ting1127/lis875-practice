votes = {'dark mode': 0, 'export': 0, 'search': 0}

def add_vote(feature):
    votes[feature] = votes[feature] + 1

def total_votes():
    return votes['dark mode'] + votes['export'] + votes['search']

for i in range(3):
    answer = input('Which feature do you want? ').lower()
    if answer == 'dark mode' or answer == 'export' or answer == 'search':
        add_vote(answer)
    else:
        print('Not on the list')

print('Results:', votes)
print('Total votes:', total_votes())
