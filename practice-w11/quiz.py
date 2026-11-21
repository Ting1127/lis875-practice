with open('vocab.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line =  line.strip()
        parts = line.split(' = ')
        print(parts)