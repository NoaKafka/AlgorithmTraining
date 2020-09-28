summ = 0
for i in range(10):
    t = summ
    summ += int(input())
    if summ >= 100:
        if abs(100 - t) < abs(100 - summ):
            print(t)
            break
        else :
            print(summ)
            break
    if i == 9:
        print(summ)
