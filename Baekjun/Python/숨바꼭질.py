# 수빈이는 동생과 숨바꼭질을 하고 있다. 
# 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 
# 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 
# 수빈이는 걷거나 순간이동을 할 수 있다. 
# 만약, 수빈이의 위치가 X일 때 걷는다면 
# 1초 후에 X-1 또는 X+1로 이동하게 된다. 
# 순간이동을 하는 경우에는 
# 1초 후에 2*X의 위치로 이동하게 된다.

# 수빈이와 동생의 위치가 주어졌을 때, 
# 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 
# 몇 초 후인지 구하는 프로그램을 작성하시오.

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
