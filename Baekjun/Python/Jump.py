#4
#2 3 3 1
#1 2 1 3
#1 2 3 1
#3 1 1 0

N = int(input())
graph = []
answer = 0
for _ in range(N):
    graph.append(list(map(int, input().split())))

visited = []
for _ in range(N):
    visited.append([ 0 ] *  N)
for x in reversed(range(N-1)):
    y = N
    for j in range(N-x):
        y -= 1
        # 작업진행
        value = graph[x][y]
        #right check
        if x + value < N:
            if visited[x + value][y] == 0:
                if x + value == N-1 and y == N-1:
                    visited[x][y] = 1
            else :
                visited[x][y] += visited[x + value][y]
            
        #down check
        if y + value < N:
            if visited[x][y + value] == 0:
                if y + value == N-1 and x == N-1:
                    visited[x][y] = 1
            else :
                visited[x][y] += visited[x][y + value]

                
        x += 1
        
for x in reversed(range(1,N-1)):
    y = 0
    for _ in range(x+1):
        
        # 작업 진행
        value = graph[x][y]
        #right check
        if x + value < N:
            if visited[x + value][y] == 0:
                if x + value == N-1 and y == N-1:
                    visited[x][y] = 1
            else :
                visited[x][y] += visited[x + value][y]
            
        #down check
        if y + value < N:
            if visited[x][y + value] == 0:
                if y + value == N-1 and x == N-1:
                    visited[x][y] = 1
            else :
                visited[x][y] += visited[x][y + value]
        
        y += 1
        x -= 1

print(visited[0][graph[0][0]] + visited[graph[0][0]][0])
