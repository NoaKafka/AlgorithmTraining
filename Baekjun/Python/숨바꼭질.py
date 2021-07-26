from collections import deque

me, sister = input().split()
me = int(me)
sister = int(sister)

out  = False
cnt = 0
q = deque()
q.append(me)

visited = dict()

while 1:
    arr_temp = []
    while len(q) != 0 :
        me = q.popleft()
        visited[me] = 1
        if me == sister:
            out = True
            break
        if me+1 == sister or me-1 == sister or me*2 == sister:
            out = True
            cnt += 1
            break

        if me != 0 :
            if me-1 not in visited :
                arr_temp.append(me-1)
            if me < sister:
                if me*2 not in visited :
                    arr_temp.append(me*2)
                if me+1 not in visited :
                    arr_temp.append(me+1)
        else:
            if me+1 not in visited :
                arr_temp.append(me+1)
        
        if len(q) == 0:
            for i in range(0, len(arr_temp)):
                q.append(arr_temp[i])
            arr_temp = []
            cnt += 1
    if out == True:
        break
    
print(cnt)
