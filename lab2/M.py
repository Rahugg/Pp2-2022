dates = []

while 1:
    inp = input().split()
    if inp[0] == '0':
        break
    dates.append((inp[0], inp[1], inp[2]))

dates = sorted(dates, key = lambda x: (x[2], x[1], x[0]))
for i in dates:
    print(*i)