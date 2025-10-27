x = 1
total = 0
while x <= 52:
    if x == 1:
        inc = 1000

    elif x > 1:
        inc = inc * 2
        total = inc * 2
    print(total)
