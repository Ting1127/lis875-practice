feature = {'name': 'Dark mode', 'status': 'in progress', 'owner': 'Jennie', 'priority': 2}

print(feature['name'])
print('Owner:' +feature['owner'])

if feature['status'] == 'done':
    print('Ready to ship!')
else:
    print('Still working on it.')