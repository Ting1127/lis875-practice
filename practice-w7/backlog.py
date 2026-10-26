backlog = [
    {'name': 'Dark mode', 'status': 'done', 'owner': 'Jennie'},
    {'name': 'Search bar', 'status': 'in progress', 'owner': 'Shaq'},
    {'name': 'Export to PDF', 'status': 'todo', 'owner': 'Kilian'},
]
wanted = input('Show which status?'). lower()

for feature in backlog:
    if feature['status'] == wanted:
        print(feature['name'], '-', feature['status'])