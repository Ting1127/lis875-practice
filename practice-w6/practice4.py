def make_ticket(feature, owner):
    return '[TODO]' + feature + ' -owner: ' + owner

features = ['login', 'search', 'dark mode']

for f in features:
    ticket = make_ticket(f, 'Jennie')
    print(ticket)
