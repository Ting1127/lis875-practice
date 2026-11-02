import time

seconds_left = 3

while seconds_left > 0:
    print('Launch in', seconds_left)
    time.sleep(1)
    seconds_left = seconds_left - 1

print('Shipped!')