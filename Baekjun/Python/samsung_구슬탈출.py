import copy
from collections import deque

def down(graph):
    [Rx, Ry, Bx, By] = findxy(graph)
    k = [Rx, Ry, Bx, By]

    if Ry == By:
        if Rx < Bx:
            #B 먼저 움직
            graph[Bx][By] = '.'
            for i in range(Bx+1, len(graph)):
                if graph[i][By] != '.':
                    if graph[i][By] == 'O':
                        return -1
                    elif graph[i][By] == '#':
                        graph[i-1][By] = 'B'
                        break
            #R 움직
            graph[Rx][Ry] = '.'
            for i in range(Rx+1, len(graph)):
                if graph[i][Ry] != '.':
                    if graph[i][Ry] == 'O':
                        return 2
                    elif graph[i][Ry] == '#' or graph[i][Ry] == 'B':
                        graph[i-1][Ry] = 'R'
                        break
            bigyo = findxy(graph)
            if bigyo == k:
                return -1
            return 1

    graph[Bx][By] = '.'
    graph[Rx][Ry] = '.'

    R_check = False
    for i in range(Rx+1, len(graph)):
        if graph[i][Ry] != '.':
            if graph[i][Ry] == 'O':
                k[0] = i
                k[1] = Ry
                R_check = True
                break
            elif graph[i][Ry] == '#':
                graph[i-1][Ry] = 'R'
                break
    for i in range(Bx+1, len(graph)):
        if graph[i][By] != '.':
            if graph[i][By] == 'O':
                return -1
            elif graph[i][By] == '#' or graph[i][By] == 'R':
                graph[i-1][By] = 'B'
                break

    if R_check == True :
        return 2
    else :
        bigyo = findxy(graph)
        if bigyo == k:
            return -1
        return 1


def up(graph):
    [Rx, Ry, Bx, By] = findxy(graph)
    k =  [Rx, Ry, Bx, By]
    if Ry == By:
        if Rx > Bx:
            #B 먼저 움직
            graph[Bx][By] = '.'
            for i in range(Bx-1, -1, -1):
                if graph[i][By] != '.':
                    if graph[i][By] == 'O':
                        return -1
                    elif graph[i][By] == '#':
                        graph[i+1][By] = 'B'
                        break
            #R 움직
            graph[Rx][Ry] = '.'
            for i in range(Rx-1, -1, -1):
                if graph[i][Ry] != '.':
                    if graph[i][Ry] == 'O':
                        return 2
                    elif graph[i][Ry] == '#' or graph[i][Ry] == 'B':
                        graph[i+1][Ry] = 'R'
                        break
            bigyo = findxy(graph)
            if bigyo == k:
                return -1

            return 1

    graph[Bx][By] = '.'
    graph[Rx][Ry] = '.'
    R_check = False
    for i in range(Rx-1, -1, -1):
        if graph[i][Ry] != '.':
            if graph[i][Ry] == 'O':
                R_check = True
                k[0] = i
                k[1] = Ry
                break
            elif graph[i][Ry] == '#' :
                graph[i+1][Ry] = 'R'
                break

    for i in range(Bx-1, -1, -1):
        if graph[i][By] != '.':
            if graph[i][By] == 'O':
                return -1
            elif graph[i][By] == '#' or graph[i][Ry] == 'R':
                graph[i+1][By] = 'B'
                break
    
    if R_check == True :
        return 2
    else :
        bigyo = findxy(graph)
        if bigyo == k:
            return -1
        return 1
    


def left(graph):
    [Rx, Ry, Bx, By] = findxy(graph)
    k = [Rx, Ry, Bx, By]
    if Rx == Bx:
        if Ry > By:
            #B 먼저 움직
            graph[Bx][By] = '.'
            for i in range(By-1, -1, -1):
                if graph[Bx][i] != '.':
                    if graph[Bx][i] == 'O':
                        return -1
                    elif graph[Bx][i] == '#':
                        graph[Bx][i+1] = 'B'
                        break
            #R 움직
            graph[Rx][Ry] = '.'
            for i in range(Ry-1, -1, -1):
                if graph[Rx][i] != '.':
                    if graph[Rx][i] == 'O':
                        return 2
                    elif graph[Rx][i] == '#' or graph[Rx][i] == 'B':
                        graph[Rx][i+1] = 'R'
                        break

            bigyo = findxy(graph)
            if bigyo == k:
                return -1
            return 1

    graph[Bx][By] = '.'
    graph[Rx][Ry] = '.'
    R_check = False
    for i in range(Ry-1, -1, -1):
        if graph[Rx][i] != '.':
            if graph[Rx][i] == 'O':
                k[0] = Rx
                k[1] = i
                R_check =True
                break
            elif graph[Rx][i] == '#':
                graph[Rx][i+1] = 'R'
                break
    for i in range(By-1, -1, -1):
        if graph[Bx][i] != '.':
            if graph[Bx][i] == 'O':
                return -1
            elif graph[Bx][i] == '#' or graph[Bx][i] == 'R':
                graph[Bx][i+1] = 'B'
                break
    if R_check == True:
        return 2
    else :
        bigyo = findxy(graph)
        if bigyo == k:
            return -1
        return 1


def right(graph):
    [Rx, Ry, Bx, By] = findxy(graph)
    k = [Rx, Ry, Bx, By]
    if Rx == Bx:
        if Ry < By:
            #B 먼저 움직
            graph[Bx][By] = '.'
            for i in range(By+1, len(graph[0])):
                if graph[Bx][i] != '.':
                    if graph[Bx][i] == 'O':
                        return -1
                    if graph[Bx][i] == '#':
                        graph[Bx][i-1] = 'B'
                        break
            #R 움직
            graph[Rx][Ry] = '.'
            for i in range(Ry+1, len(graph[0])):
                if graph[Rx][i] != '.':
                    if graph[Rx][i] == 'O':
                        return 2
                    elif graph[Rx][i] == '#' or graph[Rx][i] == 'B':
                        graph[Rx][i-1] = 'R'
                        break

            bigyo = findxy(graph)
            if bigyo == k:
                return -1
            return 1

    R_check = False
    graph[Bx][By] = '.'
    graph[Rx][Ry] = '.'
    for i in range(Ry+1, len(graph[0])):
        if graph[Rx][i] != '.':
            if graph[Rx][i] == 'O':
                k[0] = Rx
                k[1] = i
                R_check =True
                break
            elif graph[Rx][i] == '#':
                graph[Rx][i-1] = 'R'
                break
    for i in range(By+1, len(graph[0])):
        if graph[Bx][i] != '.':
            if graph[Bx][i] == 'O':
                return -1
            elif graph[Bx][i] == '#' or graph[Bx][i] == 'R':
                graph[Bx][i-1] = 'B'
                break
    
    
    if R_check == True :
        return 2
    else :
        bigyo = findxy(graph)
        if bigyo == k:
            return -1
        return 1



def findxy(graph):
    Rx = 0
    Ry = 0
    Bx = 0
    By = 0
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] == 'R':
                Rx = i
                Ry = j
            if graph[i][j] == 'B':
                Bx = i
                By = j
    return [Rx, Ry, Bx, By]


def bfs(queue):
    cnt = 1
    temp_queue = deque()
    b_queue = deque()
    b_queue.append('z')
    while True:
        if cnt > 10:
            return -1
        
        while len(queue) != 0:
            graph = copy.deepcopy(queue.popleft())
            
            temp1 = copy.deepcopy(graph)
            temp2 = copy.deepcopy(graph)
            temp3 = copy.deepcopy(graph)
            temp4 = copy.deepcopy(graph)

            arr = [up(temp1), down(temp2), left(temp3), right(temp4)]

            B = b_queue.popleft()
            for i in range(len(arr)):
                if arr[i] == 2:
                    return cnt
                elif arr[i] == 1:
                    if i == 0 and B != 'd':
                        temp_queue.append(temp1)
                        b_queue.append('u')
                    elif i == 1 and B != 'u':
                        temp_queue.append(temp2)
                        b_queue.append('d')
                    elif i == 2 and B != 'r':
                        temp_queue.append(temp3)
                        b_queue.append('l')
                    elif i == 3 and B != 'l':
                        temp_queue.append(temp4)
                        b_queue.append('r')

        if len(temp_queue) == 0:
            return -1
        queue = copy.deepcopy(temp_queue)
        temp_queue = deque()
        cnt += 1

    return -1
        
    
n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(str, input())))

queue = deque()
queue.append(graph)
answer = bfs(queue)
print(answer)
