def count_requests(items):
    tally ={}
    for r in items:
        if r not in tally:
            tally[r] = 0
        tally[r] = tally[r] + 1
    return tally

requests = ['dark mode', 'export', 'dark mode', 'search', 'dark mode', 'export']
result = count_requests(requests)
print(result)
