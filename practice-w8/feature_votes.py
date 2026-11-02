requests = ['dark mode', 'export', 'dark mode', 'search', 'dark mode', 'export']
tally = {}

for r in requests:
    if r not in tally:
        tally[r] = 0
    tally[r] = tally[r] + 1

print(tally)

