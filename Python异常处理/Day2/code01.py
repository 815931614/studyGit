ddd = {"a" : 1,"b":2,"C":3}
di =ddd.__iter__()

while True:
    try:
        print(ddd[di.__next__()])
    except StopIteration:
        break