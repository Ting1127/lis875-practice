brand = {'hermès': 0, 'chanel': 0, 'louis vuitton': 0, 'gucci': 0}

with open('answer.txt', encoding='utf-8') as f:
    text = f.read().lower()
print(text)

for name in brand:
    brand[name] = text.count(name)
print(brand)
