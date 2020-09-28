import copy
import itertools

def dfs(board, x, y):
    board[x][y] = 2
    
    if 0 < x:
        #상탐색
        if board[x-1][y] == 0:
            board = dfs(board, x-1, y)
    if x < N-1:
        #하탐색
        if board[x+1][y] == 0:
            board = dfs(board, x+1, y)
    if 0 < y:
        #좌탐색
        if board[x][y-1] == 0:
            board = dfs(board, x, y-1)
    if y < M-1:
        #우탐색
        if board[x][y+1] == 0:
            board = dfs(board, x, y+1)
            
    return board #0의 갯수


[N, M] = map(int, input().split())

board = []
for i in range(N):
    board.append(list(map(int, input().split())))

viruses = []
#find viruses
for i in range(N):
    for j in range(M):
        if board[i][j] == 2:
            viruses.append([i, j])

cleans = []
#find clean area
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            cleans.append([i, j])

#cleans 중에 조합으로 3개 뽑기
num = 3
combi = list(itertools.combinations(cleans, num))
answer = 0
for c in combi:
    m = copy.deepcopy(board)
    for xy in c:
        m[xy[0]][xy[1]] = 1

    for virus in viruses:
        m = dfs(m, virus[0], virus[1])
            
    temp_ans = 0
    for i in range(N):
        for j in range(M):
            if m[i][j] == 0:
                temp_ans += 1

    if temp_ans > answer:
        answer = temp_ans

print(answer)




