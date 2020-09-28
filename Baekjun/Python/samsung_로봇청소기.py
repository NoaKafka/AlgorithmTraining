N, M = map(int, input().split())
x,y,d = map(int, input().split())

answer = 0
board = []
for i in range(N):
    board.append(list(map(int, input().split())))


def simulate():
    global board;global x;global y;global d;global N;global M
    #step 1
    board[x][y] = 2
    #print(board)
    
    #step 2
    for i in range(4):        
        #turn left
        d -= 1
        if d < 0:
            d = 3
        if d == 0:
            # up
            if x > 0:
                if board[x-1][y] == 0:
                    x -= 1
                    return True
                
        elif d == 1:
            # right
            if y < M - 1:
                if board[x][y+1] == 0:
                    y += 1
                    return True
        elif d == 2:
            # down
            if x < N - 1:
                if board[x+1][y] == 0:
                    x += 1
                    return True
        else:
            # left
            if y > 0:
                if board[x][y-1] == 0:
                    y -= 1
                    return True
    if d == 0:
        if x < N - 1:
            if board[x+1][y] != 1:
                x += 1
                return True
            else :
                return False
    elif d == 1:
        if y > 0:
            if board[x][y-1] != 1:
                y -= 1
                return True
            else:
                return False
        else:
            return False
    elif d == 2:
        if x > 0:
            if board[x-1][y] != 1:
                x -= 1
                return True
            else :
                return False
        else :
            return False
    else :
        if y < M - 1:
            if board[x][y+1] != 1:
                y += 1
                return True
            else :
                return False
        else :
            return False

while True:
    if simulate() == False:
        break
answer = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 2:
            answer += 1
print(answer)
