def get_priority(severity):
    if severity == 1:
        return 'P0'
    elif severity == 2:
        return 'P1'
    else:
        return 'P2'

level = int(input('Bug severity (1-3): '))
priority = get_priority(level)
print('This bug is', priority)

    