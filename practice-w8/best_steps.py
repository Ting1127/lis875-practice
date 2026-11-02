steps = {'Mon': 364, 'Tue':7784, 'Wed': 5292, 'Thu':5671, 'Fri': 10106}

def best_day(week):
    top_day = ""
    top_steps = 0
    for d in week:
        if week[d] > top_steps:
            top_steps = week[d]
            top_day = d
    return top_day

winner = best_day(steps)
print('Most steps:', winner, steps[winner])
    
