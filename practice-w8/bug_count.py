def count_bug(reports):
    board ={}
    for b in reports:
        if b not in board:
            board[b] = 0
        board[b] = board[b] + 1
    return board

bugs = ['login', 'payment', 'login', 'search', 'login']
result = count_bug(bugs)
print(result)
