votes = {'dark mode': 0, 'export': 0, 'favorite': 0}

def add_vote(feature):
    votes[feature] = votes[feature] + 1

answers = ['dark mode', 'export', 'dark mode', 'favorite']

for a in answers:
    add_vote(a)

print(votes)