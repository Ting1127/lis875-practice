feature = {'name': 'Dark mode', 'status': 'in progress', 'owner': 'Jennie'}

print('Before:', feature)

new_status = input('New status: ').lower()
feature['status'] = new_status

feature['deadline'] = 'Nov 15'

print('After:', feature)

if feature['status'] == 'done':
    print('Ready to ship!')
else:
    print('Still working on it.')