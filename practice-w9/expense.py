spending = {'food': 0, 'transport': 0, 'other': 0}

def add_expense(category, amount):
    spending[category] = spending[category] + amount

def total():
    return spending['food'] + spending['transport'] + spending['other']

for i in range(3):
    category = input('category(food / transport / other):').lower()
    amount = int(input('amount: '))
    add_expense(category, amount)

print(spending)
print("Today's expense", total(), 'dollars')



